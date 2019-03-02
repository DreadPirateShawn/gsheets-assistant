SPREADSHEET=

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
	docker run -it --volume $(shell pwd)/dist:/gsheets-assistant/dist gsheets-assistant --demo --spreadsheet $(SPREADSHEET)

