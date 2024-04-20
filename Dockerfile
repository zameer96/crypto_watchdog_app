# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
