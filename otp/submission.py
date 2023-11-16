import argparse
import time
import pyotp
import qrcode

# adjust security key and user here, only use characters A-Z and 2-7
SECRET_KEY = "SHHHHTHISISASECRET"  # Replace with your secret key
USER_ID = "SECRETAGENT"         # Replace with your user ID

def generate_qr():
    # Use pyotp to generate uri
    totp = pyotp.TOTP(SECRET_KEY)
    uri = totp.provisioning_uri(name=USER_ID, issuer_name="YourApp")

    # use qrcode module to make a qrcode from the uri
    qr = qrcode.QRCode(
        # don't need a large qr code for out purposes
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Create a png from the QR code and save it
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    print("QR code generated. Check directory for qr_code.png")


def get_otp():
    # use totp app to retrieve the current time based password
    totp = pyotp.TOTP(SECRET_KEY)
    # Get the current time and print OTP based on it
    otp = totp.now()
    print("Current password:", otp)

    # sychronize 30 second timer with current time so that passwords are printed at seconds :00 and :30
    current_time = time.time()
    seconds_until_next_interval = 30 - (current_time % 30)
    time.sleep(seconds_until_next_interval)
    while True:
        # Generate and print the current OTP using the date api
        otp = totp.now()
        print("One time password:", otp)
        time.sleep(30)


if __name__ == "__main__":
    # set up args for cli usage
    parser = argparse.ArgumentParser(description="GA CLI to develop tool")
    parser.add_argument("--generate-qr", action="store_true",
                        help="Generates QR code")
    parser.add_argument("--get-otp", action="store_true", 
                        help="Generates OTP")

    args = parser.parse_args()

    if args.generate_qr:
        generate_qr()
    elif args.get_otp:
        print('to end the program hit "control + c"')
        get_otp()
    else:
        print("the only allowed flags are the following: --generate-qr or --get-otp")
