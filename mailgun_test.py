import requests
import os

# Use environment variables for sensitive credentials
MAILGUN_API_URL = os.getenv("MAILGUN_API_URL")
FROM_EMAIL_ADDRESS = os.getenv("MAILGUN_FROM_EMAIL")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")


def send_email(to_address: str, subject: str, message: str):
    resp = requests.post(
        MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL_ADDRESS,
            "to": to_address,
            "subject": subject,                                    
            "text": message
        }
    )

    if resp.status_code == 200:
        print("Success! Email sent.")


if __name__ == "__main__":
    send_email("shashanksbidarur@gmail.com","This is a test email","This is a test message.")