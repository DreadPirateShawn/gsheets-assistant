FROM ubuntu:18.04

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get -q install -y python-pip \
    && pip install --upgrade pip \
    && apt-get autoremove -q -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV WORKSPACE /gsheets-assistant
ADD . $WORKSPACE
ENV PYTHONPATH $WORKSPACE:/usr/local/lib/python2.7/dist-packages:${PYTHONPATH}
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/usr/bin/python", "/gsheets-assistant/entrypoint.py"]
CMD ["--help"]
