from pathlib import Path
import subprocess
import time

GIMP_PATH = Path(
    r"C:\Users\Duncan Doyon\AppData\Local\Programs\GIMP 2\bin\gimp-2.10.exe"
)

image_path = input("Paste the full path to your test image: ").strip().strip('"')
image_path = Path(image_path)

print("GIMP exists:", GIMP_PATH.is_file())
print("Image exists:", image_path.is_file())

if not GIMP_PATH.is_file():
    print("GIMP executable path is incorrect.")
elif not image_path.is_file():
    print("Image path is incorrect.")
else:
    try:
        # Use Windows to launch GIMP with the image.
        process = subprocess.Popen(
            [str(GIMP_PATH), str(image_path.resolve())],
            cwd=str(GIMP_PATH.parent),
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
        )

        print("Started process:", process.pid)
        time.sleep(3)

        if process.poll() is None:
            print("GIMP process is still running.")
        else:
            print("GIMP exited with code:", process.returncode)

    except Exception as error:
        print("Launch error:", repr(error))

input("Press Enter to close this test...")
