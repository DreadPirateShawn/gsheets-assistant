FROM ubuntu:18.04 AS gsheets-assistant-baseline

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get -q install -y python-pip \
    && pip install --upgrade pip \
    && apt-get autoremove -q -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV WORKSPACE /gsheets-assistant
WORKDIR $WORKSPACE
ADD . $WORKSPACE
ENV PYTHONPATH $WORKSPACE:/usr/local/lib/python2.7/dist-packages:${PYTHONPATH}
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/usr/bin/python", "/gsheets-assistant/entrypoint.py"]
CMD ["--help"]


###############
# Tests

FROM gsheets-assistant-baseline AS gsheets-assistant-tests

RUN /usr/bin/python -m unittest discover --start-directory=tests


###############
# Packaging

FROM gsheets-assistant-tests AS gsheets-assistant-package

RUN /usr/bin/python setup.py test bdist_egg
#RUN /usr/bin/python setup.py bdist_egg
