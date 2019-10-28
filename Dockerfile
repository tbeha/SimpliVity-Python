# User Ubuntu as the base Image
FROM ubuntu
#
LABEL maintainer="Thomas Beha"
LABEL version="2.1"
LABEL copyright="Thomas Beha, 2019"
LABEL license="GNU General Public License v3"
LABEL DESCRIPTION="SimpliVity Python Engine"
#
RUN apt-get update
RUN apt-get -y install python3.6 && \
	apt-get -y install python3-pip && \
	apt-get -y install vim && \
	apt-get -y install cron 
RUN /usr/bin/pip3 install requests && \
	/usr/bin/pip3 install fernet && \
	/usr/bin/pip3 install lxml
RUN mkdir /opt/python
COPY ./SimpliVityClass.py /opt/python
COPY ./vCenterClass.py /opt/python
#RUN echo "0 22 * * * root /usr/bin/python3 /opt/mrclean/mrclean.py" >> /etc/crontab && \
#    service cron restart
