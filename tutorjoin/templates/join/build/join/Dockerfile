FROM python:3.8-slim-buster
LABEL MAINTAINER=MP

RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient
RUN pip3 install gunicorn flask
RUN mkdir /join

WORKDIR /join/

#RUN pip3 install coderedcms 

RUN git clone https://github.com/murat-polat/JoinApp /join


RUN pip3 install -r requirements.txt



EXPOSE 5000


CMD gunicorn --bind=0.0.0.0:5000  app:app