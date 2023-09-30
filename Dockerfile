FROM ubuntu:20.04
WORKDIR /app/
RUN apt-get update
RUN apt-get install -y python3 python3-pip
COPY ./requirements.txt . 
RUN pip install -r requirements.txt
COPY . . 
CMD ["python3","./main.py"]

