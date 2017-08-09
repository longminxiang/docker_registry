FROM centos

MAINTAINER Eric Lung <longminxiang@163.com>

COPY ./conf /

RUN (sed -i '/enabled=1/s/1/0/g' /etc/yum/pluginconf.d/fastestmirror.conf &&\
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo &&\
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo &&\
yum clean all &&\
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

ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

VOLUME [ "/sys/fs/cgroup" ]

EXPOSE 22

ENTRYPOINT ["sh", "/run.sh"]