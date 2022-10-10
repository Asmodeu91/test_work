FROM python:3.9
WORKDIR /app
#COPY requirements.txt requirements.txt
RUN pip3 install -r psycopg2-binary
COPY . .
CMD [ "python3", "app.py"]
