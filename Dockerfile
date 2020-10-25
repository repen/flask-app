#docker build -t flask_app:latest .
#docker run --name test_app -d -p 8120:5000 flask_app:latest
#docker run --name test_app -d -v volume:/site/data -p 8120:5000 flask_app:latest
FROM python:3.6-alpine

ENV BASE_DIR /site
ENV EXTERNAL_WORK true

WORKDIR ${BASE_DIR}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app ${BASE_DIR}

CMD python main.py