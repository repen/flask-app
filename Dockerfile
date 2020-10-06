#docker build -t flask_app:latest .
#docker run --name test_app -v flaskdata:/flaskdata -d -p 8120:5000 flask_app:latest
FROM python:3.6-alpine

#VOLUME /flaskdata/

ENV APP_DIR /site
ENV DATA /flaskdata
WORKDIR ${APP_DIR}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app ${APP_DIR}/app
ENV WORK_DIR ${APP_DIR}/app

WORKDIR ${WORK_DIR}
CMD python main.py