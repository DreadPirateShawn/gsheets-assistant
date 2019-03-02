import os

from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage

#######################################
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/<CREDS_FILE>
#
# List of scopes:
#   https://developers.google.com/identity/protocols/googlescopes
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
#SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
CREDS_FILE = 'sheets.googleapis.com-gsheets_assistant.json'


class Credentials(object):

    local_path = None
    store = None
    creds = None

    def __init__(self):
        # Set local cred path
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        self.local_path = os.path.join(credential_dir, CREDS_FILE)
        self.store = Storage(self.local_path)


    def setup_local_storage(self):
        """Initialize stored credentials."""
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME

        # Original example supports Python 2.6 here, but I've dropped that as unnecessary.
        # Drop the 'noauth_local_webserver' to make this open a confirmation page in your web browser,
        #   but realistically we'll always be running this from a VM.
        flags = tools.argparser.parse_args(args=['--noauth_local_webserver'])
        credentials = tools.run_flow(flow, self.store, flags)
        print('Stored credentials to ' + self.local_path)
        return credentials


    def get(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        credentials = self.store.get()

        if not credentials or credentials.invalid:
            credentials = self.setup_local_storage()

        return credentials

