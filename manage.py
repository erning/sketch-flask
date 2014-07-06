# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.script import Server
from flask.ext.assets import ManageAssets

from application import app

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0'))
manager.add_command('assets', ManageAssets())


def main():
    manager.run()

if __name__ == '__main__':
    import sys
    sys.exit(main())

__all__ = []

# ve python manage.py assets --parse-templates build