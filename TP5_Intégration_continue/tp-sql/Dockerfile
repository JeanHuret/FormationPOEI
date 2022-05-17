FROM gradle

RUN mkdir /home/gradle/project
RUN mkdir /home/gradle/build
COPY /app-python/ /home/gradle

RUN apt update -yq && apt install -yq python3 python3-pip
RUN apt-get install -y flake8

CMD gradle packageApp