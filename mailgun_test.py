import requests
import os

MAILGUN_API_URL=os.getenv("MAILGUN_API_URL")
FROM_EMAIL_ADDRESS=os.getenv("MAILGUN_FROM_EMAIL")


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


send_email("shashanksbidarur@gmail.com","This is a test email","This is a test message.")