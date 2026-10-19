
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    send_from_directory,
)
from PIL import Image, ImageOps, ImageEnhance
from werkzeug.utils import secure_filename
from pathlib import Path
import os
import subprocess
import uuid

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
PROCESSED_DIR = BASE_DIR / "processed"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.environ.get(
    "KIOSK_SECRET_KEY",
    "dev-only-change-me",
)
app.config["MAX_CONTENT_LENGTH"] = 12 * 1024 * 1024

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}

# Your GIMP 2.10 executable
GIMP_PATH = Path(
    r"C:\Users\Duncan Doyon\AppData\Local\Programs\GIMP 2\bin\gimp-2.10.exe"
)

# --------------------------------------------------
# GIMP INTEGRATION
# --------------------------------------------------

def open_in_gimp(image_path):
    """Open the original uploaded photo in GIMP."""

    image_path = Path(image_path).resolve()

    print(f"GIMP executable: {GIMP_PATH}", flush=True)
    print(f"GIMP exists: {GIMP_PATH.is_file()}", flush=True)
    print(f"Image: {image_path}", flush=True)
    print(f"Image exists: {image_path.is_file()}", flush=True)

    if not GIMP_PATH.is_file():
        raise FileNotFoundError(
            f"GIMP executable not found: {GIMP_PATH}"
        )

    if not image_path.is_file():
        raise FileNotFoundError(
            f"Uploaded image not found: {image_path}"
        )

    # Launch GIMP with the original photo.
    process = subprocess.Popen(
        [str(GIMP_PATH), str(image_path)],
        cwd=str(GIMP_PATH.parent),
    )

    print(
        f"GIMP launch requested. Process ID: {process.pid}",
        flush=True,
    )


# --------------------------------------------------
# FILE VALIDATION AND CLEANUP
# --------------------------------------------------

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


def clear_session_files():
    """Delete only the temporary files belonging to this session."""

    for key in ("original_file", "processed_file"):
        name = session.pop(key, None)

        if name:
            for folder in (UPLOAD_DIR, PROCESSED_DIR):
                try:
                    (folder / name).unlink(missing_ok=True)
                except OSError:
                    app.logger.exception(
                        "Could not delete temporary image: %s",
                        name,
                    )


# --------------------------------------------------
# MAIN KIOSK PAGE
# --------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        step=session.get("step", "welcome"),
        original_file=session.get("original_file"),
        processed_file=session.get("processed_file"),
        payment_confirmed=session.get(
            "payment_confirmed", False
        ),
        message=session.pop("message", None),
    )


# --------------------------------------------------
# START SESSION
# --------------------------------------------------

@app.route("/start", methods=["POST"])
def start():
    clear_session_files()

    session["step"] = "upload"
    session["payment_confirmed"] = False
    session["message"] = "Welcome! Upload a photo to begin."

    return redirect(url_for("index"))


# --------------------------------------------------
# CUSTOMER PHOTO UPLOAD
# --------------------------------------------------

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("photo")

    if not file or not file.filename:
        flash("Choose a photo before continuing.", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash(
            "Use a PNG, JPG, JPEG, WEBP, or BMP image.",
            "error",
        )
        return redirect(url_for("index"))

    # Clear the previous images for this session.
    clear_session_files()

    unique = uuid.uuid4().hex
    safe_filename = secure_filename(file.filename)

    if not safe_filename:
        flash("The uploaded filename is invalid.", "error")
        return redirect(url_for("index"))

    original_name = f"{unique}_{safe_filename}"
    processed_name = f"{unique}_engraving_preview.png"

    original_path = UPLOAD_DIR / original_name
    processed_path = PROCESSED_DIR / processed_name

    # 1. Save the customer's original photo.
    try:
        file.save(str(original_path))
        print(f"Photo saved: {original_path}", flush=True)

    except OSError:
        app.logger.exception("Could not save uploaded photo")
        flash("The photo could not be saved.", "error")
        return redirect(url_for("index"))

    # 2. Create the existing grayscale preview.
    try:
        with Image.open(original_path) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
            image.thumbnail((1600, 1600))

            gray = ImageOps.grayscale(image)
            gray = ImageOps.autocontrast(gray)
            gray = ImageEnhance.Contrast(gray).enhance(1.25)

            gray.save(str(processed_path), format="PNG")

        print(f"Preview saved: {processed_path}", flush=True)

    except Exception:
        app.logger.exception("Could not generate grayscale preview")

        original_path.unlink(missing_ok=True)
        processed_path.unlink(missing_ok=True)

        flash(
            "That image could not be processed. Try another photo.",
            "error",
        )
        return redirect(url_for("index"))

    # 3. Open the ORIGINAL photo in GIMP on the host computer.
    gimp_error = False

    try:
        open_in_gimp(original_path)

    except Exception:
        gimp_error = True
        app.logger.exception("Could not launch GIMP")

    # 4. Save this order's filenames in the Flask session.
    # Keep the upload even if GIMP fails, so the photo isn't lost.
    session["original_file"] = original_name
    session["processed_file"] = processed_name
    session["step"] = "review"
    session["payment_confirmed"] = False

    if gimp_error:
        session["message"] = (
            "Photo received and preview created, but GIMP did not "
            "open. Check the VS Code terminal for the exact error."
        )
    else:
        session["message"] = (
            "Photo uploaded. GIMP was asked to open the original "
            "photo, and a grayscale preview was created."
        )

    return redirect(url_for("index"))


# --------------------------------------------------
# SERVE IMAGE PREVIEWS
# --------------------------------------------------

@app.route("/media/<kind>/<path:filename>")
def media(kind, filename):
    if kind not in {"uploads", "processed"}:
        return "Not found", 404

    if kind == "uploads":
        if filename != session.get("original_file"):
            return "Not found", 404
        directory = UPLOAD_DIR

    else:
        if filename != session.get("processed_file"):
            return "Not found", 404
        directory = PROCESSED_DIR

    return send_from_directory(
        directory,
        filename,
        as_attachment=False,
    )


# --------------------------------------------------
# DEMO PAYMENT
# --------------------------------------------------

@app.route("/payment", methods=["POST"])
def payment():
    if not session.get("processed_file"):
        flash("Upload and process a photo first.", "error")
        return redirect(url_for("index"))

    # Prototype only: no real payment is collected.
    session["payment_confirmed"] = True
    session["step"] = "position"
    session["message"] = (
        "DEMO PAYMENT APPROVED — no money was charged."
    )

    return redirect(url_for("index"))


# --------------------------------------------------
# DEMO CARD POSITIONING
# --------------------------------------------------

@app.route("/position", methods=["POST"])
def position():
    if not session.get("payment_confirmed"):
        flash(
            "Payment must be confirmed before the next step.",
            "error",
        )
        return redirect(url_for("index"))

    session["step"] = "ready"
    session["message"] = (
        "Demo card-position confirmation recorded."
    )

    return redirect(url_for("index"))


# --------------------------------------------------
# ENGRAVING DEMO
# --------------------------------------------------

@app.route("/engrave-demo", methods=["POST"])
def engrave_demo():
    if (
        not session.get("payment_confirmed")
        or session.get("step") != "ready"
    ):
        flash("Complete the previous steps first.", "error")
        return redirect(url_for("index"))

    # Does not activate a laser or connect to EZCAD3.
    session["step"] = "complete"
    session["message"] = (
        "DEMO COMPLETE — no laser or hardware was activated."
    )

    return redirect(url_for("index"))


# --------------------------------------------------
# RESET KIOSK SESSION
# --------------------------------------------------

@app.route("/reset", methods=["POST"])
def reset():
    clear_session_files()
    session.clear()

    session["step"] = "welcome"
    session["message"] = (
        "Session reset. Temporary prototype images were deleted."
    )

    return redirect(url_for("index"))


# --------------------------------------------------
# UPLOAD SIZE ERROR
# --------------------------------------------------

@app.errorhandler(413)
def too_large(_error):
    flash(
        "Image is too large. The upload limit is 12 MB.",
        "error",
    )
    return redirect(url_for("index"))


# --------------------------------------------------
# START FLASK
# --------------------------------------------------

if __name__ == "__main__":
    # Local development only.
    # Do not expose Flask's development server publicly.
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
    )
