# Setup

### Enable GSheets API
 - Go to: https://console.developers.google.com/apis/library
 - Select or create project from the upper left drop-down. _(Note, creating a project may require more than a standard user account.)_
 - Make sure the "Google Sheets API" is enabled.

### Create client secret
 - Go to: https://console.developers.google.com/apis/credentials
 - Create credentials ➤ OAuth client ID
 - Create an “Google Sheets API Quickstart” ID (the name itself might matter here), Type "Other UI" accessing "User data"
 - Save the “client_secret_etcblahblah.apps.googleusercontent.com.json” file

### References:
 - https://developers.google.com/sheets/api/quickstart/python
 - https://developers.google.com/api-client-library/python/auth/web-app
 - https://stackoverflow.com/questions/44448029/how-to-use-google-sheets-api-while-inside-a-google-cloud-function/51037780#51037780

# Usage

### Demo

### Build image
```
docker build . --file Dockerfile --tag gsheets-assistant
```

### Run tests
```
docker build . --file Dockerfile --tag gsheets-assistant --target gsheets-assistant-tests
```

### Build wheel
```
docker build . --file Dockerfile --tag gsheets-assistant --target gsheets-assistant-package
docker run --rm --entrypoint=/bin/tar gsheets-assistant -c -C /gsheets-assistant/dist . | tar x
```

### Installing the tool
```
pip install gsheets_assistant-$(cat VERSION)-py3-none-any.whl --upgrade
```

### Running the tool
Note that if you run this from the top level of the repo, you'll be running the raw code directly, rather than the installed wheel.
The first time you run one of these, it will prompt you to load a URL in your browser and approve, and then it'll save creds to ~/.credentials
Subsequent runs will use the saved credentials.

##### Demo: Read sample file
```
python3 -m gsheets_assistant.__demo_read__ --secret-file PATH_TO_YOUR_SECRET_FILE
```

##### Demo: Create sample sheet
Create your empty spreadsheet first, and provide the ID here.
```
python3 -m gsheets_assistant.__demo_write__ --secret-file PATH_TO_YOUR_SECRET_FILE --spreadsheet SPREADSHEET_ID
```

### Things you can do
TODO: Cheat sheet for various convenience options

### Using a virtual env
Using a virtualenv to run the tool is recommended, but of course you do you. If you're unfamiliar, here's how to use a virtualenv in Python 3.3+. The `...` below is where you'll type all the install and runtime things that you want to keep isolated from your larger system, at the `(venv)` prompt.

#####  1. Create a venv folder in the project
```
python -m venv venv
```

##### 2. Enter the venv
```
source venv/bin/activate
(venv) $ ...
```

##### 3. Exit the venv
```
(venv) $ deactivate
```
