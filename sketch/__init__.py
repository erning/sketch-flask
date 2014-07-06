# -*- coding: utf-8 -*-

import os

from flask import Flask

class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)

        # 以如下顺序读取配置文件，一个成功即返回
        # * 环境变量`SKETCH_SETTINGS`指定的配置文件
        # * `$(HOME)/.sketch.cfg`
        # * `/etc/sketch.cfg`

        from sketch import version, default_settings
        self.config.from_object(version)
        self.config.from_object(default_settings)

        if ('SKETCH_SETTINGS' in os.environ):
            self.config.from_envvar('SKETCH_SETTINGS', silent=True)
            return

        path = os.path.abspath(os.path.expanduser('~/.sketch.cfg'))
        if (os.path.isfile(path)):
            self.config.from_pyfile(path, silent=True)
            return

        self.config.from_pyfile('/etc/sketch.cfg', silent=True)

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = rule

        super(Application, self).add_url_rule(
            rule,
            endpoint=endpoint,
            view_func=view_func,
            **options
        )

app = Application(__name__)
