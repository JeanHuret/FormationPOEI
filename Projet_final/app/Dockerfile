
FROM gradle

RUN mkdir /home/gradle/project
RUN mkdir /home/gradle/build
COPY /app_python/ /home/gradle/app_python

RUN apt update -yq && apt install -y python3 python3-pip
RUN apt-get install -y flake8 && pip install flake8-html

CMD gradle packageApp