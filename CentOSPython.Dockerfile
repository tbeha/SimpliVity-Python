
# docker build -t centpy -f CentOSPython.Dockerfile . 
# Use CentOS as the base Image 
FROM  centos
LABEL maintainer="Thomas Beha"
LABEL version="2.0"
LABEL copyright="Thomas Beha, 2020"
LABEL license="GNU General Public License v3"
LABEL DESCRIPTION="CTC SimpliVity Python container based on Ubuntu"
# Install Python 3.6
#RUN yum install -y https://centos7.iuscommunity.org/ius-release-el7.rpm
RUN yum update -y
#RUN yum install -y python36u python36u-libs python36u-devel python36u-pip
RUN yum install -y python36
RUN /usr/bin/pip3.6 install --upgrade pip
# Install the necessary Python packages:
RUN /usr/bin/pip3.6 install datetime && \
    /usr/bin/pip3.6 install requests && \
	/usr/bin/pip3.6 install cryptography && \
	/usr/bin/pip3.6 install fernet && \
	/usr/bin/pip3.6 install lxml && \
	/usr/bin/pip3.6 install prometheus_client
# copy the necessary python files to the container
RUN mkdir /opt/svt
COPY ./SimpliVityClass.py /opt/python
COPY ./vCenterClass.py /opt/python
#RUN echo "0 22 * * * root /usr/bin/python3 /opt/SvtCollector.py" >> /etc/crontab && \
#    service cron restart