# -*- coding: utf-8 -*-
import os

DEFAULT_APP_NAME = 'website'

APP_ROOT = '/home/'

UWSGI_CONF_PATH = '/opt/conf/uwsgi.ini'


def get_first_dir(p):
    try:
        p = p + "/" if p[-1] != "/" else p
        a = os.listdir(p)
        for x in a:
            if os.path.isdir(p + x):
                return x
    except Exception, e:
        print e


class DjangoApp(object):

    def __init__(self):
        super(DjangoApp, self).__init__()
        self.app_name = get_first_dir(APP_ROOT)
        if self.app_name is None:
            self.app_name = DEFAULT_APP_NAME
        self.app_dir = APP_ROOT + self.app_name + "/"

    # 如果项目不存在，创建一个新项目
    def new_app_if_needed(self):
        fn = '%s%s' % (self.app_dir, 'manage.py')
        if not os.path.exists(fn):
            os.mkdir(self.app_dir)
            os.system("echo \"create new app %s\"" % self.app_name)
            os.system("django-admin.py startproject %s %s" % (self.app_name, self.app_dir))

    # 创建uwsgi配置
    def create_uwsgi_config(self):
        if os.path.exists(UWSGI_CONF_PATH):
            return
        f = open(UWSGI_CONF_PATH, 'w')
        nstr = "[uwsgi]\n \
                http = :8888\n \
                chdir = %s\n \
                wsgi-file = %s/wsgi.py\n \
                processes = 2\n \
                threads = 1\n" % (self.app_dir, self.app_name)
        f.write(nstr)
        f.close()

    def start(self):
        self.new_app_if_needed()
        os.system("echo yes | python %smanage.py collectstatic" % self.app_dir)
        self.create_uwsgi_config()
        os.system("echo \"run uwsgi\"")
        os.system("uwsgi %s" % UWSGI_CONF_PATH)

if __name__ == "__main__":
    app = DjangoApp()
    app.start()
