from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        drive_service = build('drive', 'v3', credentials=creds)

        def get_directory_structure(service, folder_id, indent, output_file):
            files = service.files().list(q=f"'{folder_id}' in parents").execute()

            # Keep track of the indentation level, which will be used to visually
            # represent the directory structure in the final text file
            indent_str = "  " * indent

            for file in files["files"]:
                # Print the current file or folder's name, along with its indentation level
                print(f"{indent_str}{file['name']}", file=output_file)

                # # If the current file is a folder, recursively call the function to traverse its contents
                if file["mimeType"] == "application/vnd.google-apps.folder":
                    get_directory_structure(service, file["id"], indent + 1, output_file)

        # Now we can open the output file and call the function to traverse the
        # directory structure and save it to the file
        with open("directory_structure.txt", "w", encoding="utf-8") as output_file:
            get_directory_structure(drive_service, "1PVE6OtUlxwfxdUT10M4ZLlOM7Fok_PjG", 0, output_file)


    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()