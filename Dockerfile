FROM ubuntu:20.04
RUN  apt-get update
RUN  apt-get install --no-install-recommends --yes python3 
COPY app.py text.txt /app/
WORKDIR /app/ 
