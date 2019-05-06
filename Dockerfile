FROM python:latest

COPY . /dumbwebhook

WORKDIR /dumbwebhook

RUN pip install -r /dumbwebhook/requirements.txt

RUN apt-get update && apt-get install -y tmux

ENTRYPOINT bash /dumbwebhook/bin/run-dumbwebhook.sh