FROM jenkins/jenkins:latest
USER root
RUN apt-get update -y 
RUN apt-get install -y python3-pip python3-dev 
RUN apt-get install -y flake8 
RUN pip install flake8-junit-report
USER jenkins
