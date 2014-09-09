# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy

class _SQLAlchemy(SQLAlchemy):
    def set_options(self, options):
        self.options = options

    def apply_driver_hacks(self, app, info, options):
        for o in self.options:
            if o not in options:
                options[o] = self.options[o]
        super(_SQLAlchemy, self).apply_driver_hacks(app, info, options)

    def commit_or_rollback(self):
        """Commits current db session or rollbacks on exception.
        """
        try:
            self.session.commit()
        except:
            self.session.rollback()
            raise


db = _SQLAlchemy()
