FROM python:3.6-alpine

VOLUME flaskdata

ENV APP_DIR /site

WORKDIR ${APP_DIR}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app ${APP_DIR}/app

ENV WORK_DIR ${APP_DIR}/app

WORKDIR ${WORK_DIR}
CMD python main.py