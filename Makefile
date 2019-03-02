SPREADSHEET=
OAUTH_CLIENT_ID=
SECRET_FILE=

all: test

image:
	docker build . -f Dockerfile -t gsheets-assistant

build: image
	mkdir -p $(shell pwd)/dist
	docker run -it --volume $(shell pwd)/dist:/gsheets-assistant/dist gsheets-assistant --build

test: image
	docker run -it gsheets-assistant --test

testpackage: image
	docker run -it --volume $(shell pwd)/dist:/gsheets-assistant/dist gsheets-assistant --test-package

demo: image
	mkdir -p ~/.credentials
	docker run -it --volume $(shell pwd)/dist:/gsheets-assistant/dist --volume ~/.credentials:/root/.credentials --volume $(SECRET_FILE):/gsheets-assistant/client_secret.json gsheets-assistant --demo --spreadsheet $(SPREADSHEET) --secret-file /gsheets-assistant/client_secret.json --oauth-client-id "$(OAUTH_CLIENT_ID)"

compare:
	docker build . -f Dockerfile_compare -t gsheets-assistant-compare
	mkdir -p ~/.credentials
	docker run -it --volume $(shell pwd)/dist:/gsheets-assistant/dist --volume ~/.credentials:/root/.credentials --volume $(SECRET_FILE):/gsheets-assistant/client_secret.json gsheets-assistant-compare --compare --spreadsheet $(SPREADSHEET) --secret-file /gsheets-assistant/client_secret.json --oauth-client-id "$(OAUTH_CLIENT_ID)"
