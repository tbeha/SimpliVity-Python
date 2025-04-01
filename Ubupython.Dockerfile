# User Ubuntu as the base Image
FROM ubuntu
#
LABEL maintainer="Thomas Beha"
LABEL version="3.0"
LABEL copyright="Thomas Beha, 2020"
LABEL license="GNU General Public License v3"
LABEL DESCRIPTION="CTC SimpliVity Python container based on Ubuntu"
#
RUN apt-get update
RUN apt-get -y install python3.6 && \
	apt-get -y install python3-pip && \
	apt-get -y install vim && \
	apt-get -y install cron 
RUN /usr/bin/pip3 install requests && \
	/usr/bin/pip3 install fernet && \
	/usr/bin/pip3 install cryptography && \
	/usr/bin/pip3 install lxml && \
	/usr/bin/pip3 install python-ilorest-library && \
	/usr/bin/pip3 install prometheus_client
# copy the necessary python files to the container
#RUN mkdir /opt/svt
#COPY ./SimpliVityClass.py /opt/python
#COPY ./vCenterClass.py /opt/python
#RUN echo "0 22 * * * root /usr/bin/python3 /opt/SvtCollector.py" >> /etc/crontab && \
#    service cron restart
