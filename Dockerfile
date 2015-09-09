FROM resin/raspberrypi-python:latest
MAINTAINER Jonathan Moss <jmoss@snowballone.com.au>

RUN apt-get update && apt-get install -y build-essential --no-install-recommends

COPY requirements.txt /app/requirements.txt
RUN pip install -r app/requirements.txt
COPY . /app
EXPOSE 80
CMD ["/app/bootstrap.sh"]
