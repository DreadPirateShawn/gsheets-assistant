FROM ubuntu:18.04 AS gsheets-assistant-baseline

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get -q install -y python3 python3-pip \
    && pip3 install --upgrade pip setuptools wheel \
    && apt-get autoremove -q -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV WORKSPACE /gsheets-assistant
WORKDIR $WORKSPACE
ADD . $WORKSPACE
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE true

ENTRYPOINT ["/usr/bin/python3", "/gsheets-assistant/entrypoint.py"]
CMD ["--help"]


###############
# Tests

FROM gsheets-assistant-baseline AS gsheets-assistant-tests

RUN /usr/bin/python3 -m unittest discover --start-directory=tests


###############
# Packaging

FROM gsheets-assistant-tests AS gsheets-assistant-package

RUN /usr/bin/python3 setup.py test bdist_wheel
