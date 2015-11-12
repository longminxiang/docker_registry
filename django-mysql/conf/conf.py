# -*- coding: utf-8 -*-
import os
import re

DEFAULT_APP_NAME = 'mysite'

APP_DIR = '/home/app/'
CONF_DIR = '/opt/'


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

    def start(self):
        self.new_app_if_needed()
        os.system("echo \"start django\"")
        os.system("python %s/manage.py runserver 0.0.0.0:8000" % APP_DIR)

if __name__ == "__main__":
    app = DjangoApp()
    app.start()
