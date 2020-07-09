FROM python:3.7
LABEL maintainer "Artem Kuchumov <duketemon@gmail.com>"

WORKDIR /usr/src/app
ADD knowledge_base .
RUN pip install -r requirements.txt

CMD python init_data_storage.py
