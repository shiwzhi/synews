From ubuntu:latest


RUN apt update && apt -y install python3 python3-pip python3-lxml git
RUN pip3 install beautifulsoup4 requests

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8