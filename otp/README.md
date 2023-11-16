# README for submission.py

## Two-Factor Authentication (TOTP) Python Script

This Python script, `submission.py`, provides a simple implementation of Two-Factor Authentication (TOTP - Time-based One-Time Password) using the `pyotp` library. TOTP is commonly used for enhancing the security of user authentication by generating unique passwords that expire after a short period.

### Prerequisites

Before running the script, ensure you have the necessary Python libraries installed. You can install them using the following command:

```bash
pip install pyotp qrcode[pil]
```

note: it is often recommended to use a virtual environment to install libraries

### Configuration

Adjust the following constants in the script according to your preferences:

```python
SECRET_KEY = "SHHHHTHISISASECRET"  # Replace with your secret key
USER_ID = "SECRETAGENT"             # Replace with your user ID
```

Make sure to use only characters A-Z and 2-7 for the `SECRET_KEY`.

### Usage

The script supports two main functionalities:

1. **Generate QR Code:** This function creates a QR code that can be scanned by a TOTP authenticator app, facilitating the setup of TOTP for a specific user.

   ```bash
   python submission.py --generate-qr
   ```

   The QR code image will be saved as `qr_code.png` in the script's directory.

2. **Generate OTP:** This function continuously generates and prints one-time passwords based on the TOTP algorithm. The passwords are synchronized with 30-second intervals.

   ```bash
   python submission.py --get-otp
   ```

   To end the OTP generation, press "Control + C."

### Command-Line Arguments

The script supports the following command-line arguments:

- `--generate-qr`: Generate QR code for TOTP setup.
- `--get-otp`: Generate and continuously print OTPs.

Example:

```bash
python submission.py --generate-qr
```

### Dependencies

- `pyotp`: Used for TOTP implementation -- https://pyauth.github.io/pyotp/
- `qrcode` and `pillow` (PIL): Used for generating and saving QR codes.

## SOURCES:

    an additional place I looked at to understand the implementation of the
    totp algorithm is the following blog post:
    https://drewdevault.com/2022/10/18/TOTP-is-easy.html

    I also looked at RFC 6238:
    https://tools.ietf.org/html/rfc6238

### Author

This script was created by [Sami Noor Syed].
