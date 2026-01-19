"""
Gmail Service - handles authentication and API calls.

Your tools.py will import functions from here.
"""

import os
import base64
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Need both read and compose permissions
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
]


def get_gmail_service():
    """Authenticate and return Gmail service instance."""
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def fetch_emails(n: int) -> list[dict]:
    """
    Fetch the last n emails from inbox.

    Returns list of dicts with: id, sender, subject, body, thread_id
    """
    service = get_gmail_service()

    # TODO: Your task - fill this in!
    #
    # Hints:
    # 1. Use service.users().messages().list() to get message IDs
    # 2. Use service.users().messages().get() to get full message details
    # 3. Headers contain 'From' and 'Subject'
    # 4. Body is in payload (can be nested in 'parts')
    #
    # Try to figure it out using Gmail API docs:
    # https://developers.google.com/gmail/api/reference/rest

    pass


def create_email_draft(to: str, subject: str, body: str, thread_id: str = None) -> str:
    """
    Create a draft email.

    Returns the draft ID.
    """
    service = get_gmail_service()

    # TODO: Your task - fill this in!
    #
    # Hints:
    # 1. Create a MIMEText message
    # 2. Encode it with base64.urlsafe_b64encode
    # 3. Use service.users().drafts().create()
    #
    # Gmail API docs for drafts:
    # https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create

    pass


if __name__ == "__main__":
    # Test authentication
    service = get_gmail_service()
    print("Gmail service authenticated successfully!")
