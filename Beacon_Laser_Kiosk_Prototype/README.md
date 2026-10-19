# Beacon Laser Kiosk — Prototype

A local Windows-friendly prototype for the proposed Beacon Laser Kiosk customer workflow.

## What works now
- Welcome/start screen and staged kiosk workflow
- Uploads JPG, PNG, WEBP, or BMP photos (12 MB maximum)
- Stores the original image locally for the active session
- Generates a grayscale, autocontrasted PNG preview using Pillow
- Simulates payment approval and card-position confirmation
- Guards later workflow steps so they cannot be skipped through the UI
- Reset deletes this session's original and processed image files

## Safety and scope
**This is not production kiosk software.** Payment is simulated; no Cantaloupe hardware, MDB interface, Raspberry Pi, actuator, exhaust, lighting, card dispenser, GIMP plugin, or EZCAD3 integration is connected. The final demo step does not activate a laser or hardware. Do not use this as a substitute for hardware interlocks, emergency stops, or laser safety systems.

The grayscale output is only a preview. The project coordinator's required photo-processing plugin and settings must be integrated and validated for the actual material and laser.

## Run on Windows
1. Install Python 3.11+ from python.org and enable "Add Python to PATH".
2. Extract this ZIP to a normal development folder.
3. Open that folder in Visual Studio Code.
4. Open Terminal → New Terminal.
5. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` and use `.\.venv\Scripts\python.exe app.py` below.

6. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

7. Start the app:

   ```powershell
   python app.py
   ```

8. Open http://127.0.0.1:5000 in your browser.

## Project layout
- `app.py` — Flask routes, temporary file handling, image processing, and demo workflow
- `templates/index.html` — responsive touchscreen-style interface
- `uploads/` — temporary original photos (created automatically)
- `processed/` — processed grayscale preview PNGs (created automatically)

## Next development milestones
1. Confirm supplied photo-processing plugin and required image format/settings.
2. Add kiosk-specific QR upload/session association.
3. Integrate verified Cantaloupe/MDB payment events; never treat a UI button as payment proof.
4. Define a Raspberry Pi command protocol and hardware status feedback.
5. Integrate EZCAD3 through a documented interface where available.
6. Add production-grade authentication, logging, secure temporary storage, cleanup policies, and fault recovery.
7. Validate safety interlocks and hardware behavior with the project coordinator before live tests.
