#docker build -t flask_app:latest .
#docker run --name test_app -d -p 8120:5000 flask_app:latest
#docker run --name test_app -d -v volume:/volume -p 8120:5000 flask_app:latest
FROM python:3.8


ENV DIR_SCRIPT /home/pyuser/script
RUN useradd -ms /bin/bash pyuser && mkdir ${DIR_SCRIPT}
RUN mkdir /volume
RUN chown -R pyuser:pyuser /volume
USER pyuser

ENV BASE_DIR ${DIR_SCRIPT}

WORKDIR ${BASE_DIR}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app ${DIR_SCRIPT}

CMD python main.py --config=production