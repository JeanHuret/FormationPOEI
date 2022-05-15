FROM gradle

RUN mkdir /home/gradle/project
RUN mkdir /home/gradle/build
COPY tp-sql/app-python/ /home/gradle

RUN apt update -yq && apt install -yq python3 python3-pip

CMD gradle packageApp