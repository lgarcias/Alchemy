FROM mcr.microsoft.com/devcontainers/python:3.11

# Instala dependencias del backend
COPY ../backend/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# Instala utilidades y git-flow
RUN apt-get update && apt-get install -y wget unzip git-flow

WORKDIR /workspace
