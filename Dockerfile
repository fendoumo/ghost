FROM ubuntu
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-qt4 python-ghost xvfb
VOLUME ["/var/vol/"]
ADD ghosttest.py /var/
WORKDIR /var/
CMD ["python","/var/ghosttest.py"]