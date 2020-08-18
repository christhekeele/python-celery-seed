FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# Add setup scripts
RUN mkdir /code/bin
ADD bin/* /code/bin/
RUN chmod +x /code/bin/*

# Install dependencies
ADD Pipfile* /code/
RUN /code/bin/install

# Setup app
ADD . /code/
ENV PYTHONPATH=${PYTHONPATH}:/code

# RUN command
# None supplied intentionally
