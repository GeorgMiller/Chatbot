FROM python:3.8


ENV PYTHONUNBUFFERED=1
WORKDIR /otree/

RUN apt-get update &&\
    apt-get install -y\
    bash \
    build-essential\
    gcc\
    libffi-dev\
    musl-dev\
    openssl\
    postgresql\
    libpq-dev

COPY . .
RUN pip install -r ./requirements.txt
RUN pip install python-socketio
#RUN pip3 install rasa --ignore-installed ruamel.yaml
EXPOSE 8000 5005 5055

