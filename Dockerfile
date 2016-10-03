FROM python:2.7.12
MAINTAINER Ivar Refsdal <Ivar.Refsdal@nsd.uib.no>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN virtualenv venv
COPY requirements.txt /usr/src/app/
RUN ./venv/bin/pip install -r requirements.txt

WORKDIR /usr/src/app
COPY . /usr/src/app

EXPOSE 8080
CMD [ "./venv/bin/python", "./server.py" ]
