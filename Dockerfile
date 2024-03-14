FROM python:3.9-alpine
WORKDIR /app/
COPY ./requirements.txt . 
RUN apk update
RUN pip install -r requirements.txt
COPY . . 
CMD ["python3","./main.py"]

