FROM python:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev mariadb-server build-essential 

ADD requirements.txt /

RUN pip3 install mariadb --no-cache-dir -r /requirements.txt
COPY tp-sql-python-master/app-python/ /usr/src/app/
EXPOSE 5000
CMD ["python3", "/usr/src/app/main.py"]



