# -*- coding: utf-8 -*-

from functools import wraps

from flask import current_app
from flask import json
from flask import request
from flask import jsonify as flask_jsonify

from application import app


#
# exports
#
def exports(rule, login_required=False, **options):
    def decorator(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            app.logger.debug("API: %s.%s" % (fn.__module__, fn.__name__))
            # TODO: login_required
            return fn(*args, **kwargs)

        api_rule = app.config['API_PREFIX'] + rule
        endpoint = options.pop('endpoint', api_rule)
        app.add_url_rule(api_rule, endpoint, view_func=decorated_view, **options)
        return decorated_view
    return decorator


#
# allow array at top level
# http://flask.pocoo.org/docs/security/#json-security
#
def jsonify(*args, **kwargs):
    if len(args) == 1 and type(args[0]) in (list, tuple):
        return current_app.response_class(
            json.dumps(args[0], indent=None if request.is_xhr else 2),
            mimetype='application/json'
        )
    return flask_jsonify(*args, **kwargs)