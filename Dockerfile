FROM ubuntu
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-qt4 
RUN apt-get install -y python-ghost 
RUN apt-get install -y xvfb 
VOLUME ["/var/vol/"]
ADD ghosttest.py /var/
WORKDIR /var/
CMD ["python","/var/ghosttest.py"]