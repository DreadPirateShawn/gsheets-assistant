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

### Build egg
```
docker build . --file Dockerfile --tag gsheets-assistant --target gsheets-assistant-package
docker run --rm --entrypoint=/bin/tar gsheets-assistant -c -C /gsheets-assistant/dist . | tar x
```
