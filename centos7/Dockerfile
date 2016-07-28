FROM centos:7

MAINTAINER Eric Lung <longminxiang@163.com>

COPY ./conf /

RUN (yum -y update &&\
yum -y install epel-release &&\
yum -y install openssh-server pwgen python-pip python-devel &&\
yum clean all)

RUN (cd root &&\
mkdir .pip &&\
cd .pip &&\
echo -e "\n[global]\n\
index-url = http://pypi.douban.com/simple\n\
--trusted-host = pypi.douban.com"\
>> pip.conf &&\
cd /usr/lib/python2.7/site-packages/ &&\
echo -e "import sys\n\
sys.setdefaultencoding('utf-8')"\
>> sitecustomize.py)

RUN (sed -i '/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/'d /etc/ssh/sshd_config &&\
sed -i '/HostKey \/etc\/ssh\/ssh_host_ed25519_key/'d /etc/ssh/sshd_config &&\
ssh-keygen -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key &&\
sed -i '/pam_loginuid.so/'d /etc/pam.d/sshd)

EXPOSE 22

CMD ["sh", "/run.sh"]