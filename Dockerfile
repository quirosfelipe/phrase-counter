FROM ubuntu:20.04
RUN  apt-get update
RUN  apt-get install --no-install-recommends --yes python3 
COPY app.py  /app/
WORKDIR /app/ 
ENTRYPOINT ["python3","app.py"]
CMD ["/data/origin.txt"]
