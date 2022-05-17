FROM gradle

RUN mkdir /home/gradle/project
RUN mkdir /home/gradle/build
COPY /app-python/ /home/gradle

RUN apt update -yq && apt install -y python3 python3-pip
RUN apt-get install -y flake8 && apt-get pip install flake8-junit-report

CMD gradle packageApp