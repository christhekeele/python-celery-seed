FROM python:3.9.7-alpine

# Make STDOUT work for logging
ENV PYTHONUNBUFFERED=true
# Show which packages segfaults come from
ENV PYTHONFAULTHANDLER=showsegfaults
# Show warnings, but only once
ENV PYTHONWARNINGS=once
# Set log levels
ENV LOG_LEVEL=INFO

RUN mkdir /code
WORKDIR /code

# Add system dependencies
# (used for building python dependency C extensions)
RUN apk add --no-cache bash make gcc g++ musl-dev
RUN apk add --no-cache vim curl bind-tools
RUN apk add --no-cache libxml2-dev libxslt-dev

# Add setup scripts
ADD bin /code/bin
RUN chmod u+x /code/bin/**/*

# Set up project command runner
RUN /code/bin/setup

# Add application code
ADD app /code/app
ENV PYTHONPATH=${PYTHONPATH}:app

# Add scripts
ADD scripts /code/scripts

# Install dependencies
ADD Pipfile* /code/
RUN /code/bin/install

# Pre-compile python byte code
RUN python -m compileall -x ./app/**/*.py

# Add tmp dir
ADD tmp /code/tmp

# RUN command
# None supplied intentionally
