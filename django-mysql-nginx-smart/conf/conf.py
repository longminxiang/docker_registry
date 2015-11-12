# -*- coding: utf-8 -*-
import os
import re

DEFAULT_APP_NAME = 'website'

APP_DIR = '/home/app/'
CONF_DIR = '/opt/conf/'

NGINX_CONF_NAME = 'nginx-django.conf'
NGINX_CONF_SRC = '%s%s' % (CONF_DIR, NGINX_CONF_NAME)
NGINX_CONF_DEST = '/etc/nginx/sites-enabled/%s' % NGINX_CONF_NAME

DJANGO_XML = '%s%s' % (CONF_DIR, 'django.xml')


class DjangoApp(object):

    def __init__(self):
        super(DjangoApp, self).__init__()
        self.app_name = DEFAULT_APP_NAME

    def new_app_if_needed(self):
        fn = '%s%s' % (APP_DIR, 'manage.py')
        if not os.path.exists(fn):
            os.system("echo \"create new app %s\"" % self.app_name)
            os.system("django-admin.py startproject %s %s" % (self.app_name, APP_DIR))
        else:
            output = []
            f = open(r"%s" % fn)
            for i in f.readlines():
                output.append(i)
                f.close()
            ostr = "".join(output)
            p = re.compile(r'(, ")(.*)(\.settings)')
            match = p.search(ostr)
            self.app_name = match.groups()[1]

    def app_path(self):
        return '%s%s' % (APP_DIR, self.app_name)

    def change_django_xml(self):
        output = []
        f = open(r"%s" % DJANGO_XML)
        for i in f.readlines():
            output.append(i)
            f.close()
        ostr = "".join(output)
        p = re.compile(r'(<chdir>.*</chdir>)')
        match = p.search(ostr)
        mstr = match.group()
        nstr = '<chdir>%s</chdir>' % self.app_path()
        if mstr != nstr:
            os.system("echo \"update django xml\"")
            nstr = p.sub(nstr, ostr)
            f = open(r"%s" % DJANGO_XML, 'w')
            f.write(nstr)
            f.close()

    def start(self):
        self.new_app_if_needed()
        os.system("echo \"install requirements\"")
        os.system("pip install -i http://pypi.douban.com/simple -r %srequirements.txt" % APP_DIR)
        os.system("echo yes | python /home/app/manage.py collectstatic")
        if os.path.exists(NGINX_CONF_DEST):
            os.remove(NGINX_CONF_DEST)
        os.system("ln -s %s %s" % (NGINX_CONF_SRC, NGINX_CONF_DEST))
        self.change_django_xml()
        os.system("echo \"run uwsgi\"")
        os.system("uwsgi -d %sdjango.log -x %s" % (CONF_DIR, DJANGO_XML))
        os.system("echo \"start nginx\"")
        os.system("nginx -g 'daemon off;'")

if __name__ == "__main__":
    app = DjangoApp()
    app.start()
