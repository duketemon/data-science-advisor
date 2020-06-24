FROM python:3.7
LABEL maintainer "Artem Kuchumov <duketemon@gmail.com>"

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD source source
WORKDIR /usr/src/app/source

CMD python app.py
