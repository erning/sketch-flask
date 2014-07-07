# -*- coding: utf-8 -*-

import os

from application import app

#
# jinja2 html compress
#
import jinja2htmlcompress
jinja2htmlcompress.enabled = app.debug and app.config['HTML_COMPRESS']
app.jinja_env.add_extension("jinja2htmlcompress.SelectiveHTMLCompress")


#
# web assets
#

import flask.ext.assets

webassets = flask.ext.assets.Environment(app)

webassets.url = '%s/assets' % app.config['CDN_URL_PREFIX']
webassets.append_path(os.path.abspath('%s/../templates' % app.static_folder))
webassets.append_path(os.path.abspath('%s/../bower_components' % app.static_folder))

if webassets.config.get('directory'):
    app.logger.info("assets.directory: %s" % webassets.directory)
else:
    import tempfile
    webassets.directory = tempfile.mkdtemp()
    app.logger.warn("assets.directory: %s" % webassets.directory)


#
# register global assets
#

@app.route('/assets/<path:filename>', endpoint='assets')
def _send_assets_file(filename):
    cache_timeout = app.get_send_file_max_age(filename)
    return flask.helpers.send_from_directory(
        webassets.directory, filename, cache_timeout=cache_timeout)


def register_asset(name, *asset_files):
    from webassets.filter import get_filter
    if not asset_files:
        asset_files = [name]
    bundles = []
    for asset_file in asset_files:
        _, fe = os.path.splitext(asset_file)

        if fe == '.!':
            asset_file = _
            _, fe = os.path.splitext(asset_file)
            allow_jinja2 = lambda x : x != 'jinja2'
        else:
            allow_jinja2 = lambda x : x

        if fe == '.js':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=tuple(filter(allow_jinja2, ('jinja2', 'uglifyjs')))
            )
        elif fe == '.coffee':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=tuple(filter(allow_jinja2, ('jinja2', 'coffeescript', 'uglifyjs')))
            )
        elif fe == '.css':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=tuple(filter(allow_jinja2, ('jinja2', 'cssmin')))
            )
        elif fe == '.sass':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file, '**/*.sass', '*.sass'],
                filters=tuple(filter(allow_jinja2, ('jinja2', 'compass', 'cssmin')))
            )
        elif fe == '.scss':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file, '**/*.scss', '*.scss'],
                filters=tuple(filter(allow_jinja2, ('jinja2', 'compass', 'cssmin')))
            )
        else:
            raise ValueError('%s not support', asset_file)
        bundles.append(bundle)

    fn, fe = os.path.splitext(name)
    output = '%s.%%(version)s%s' % (fn, fe)
    webassets.register(name, *bundles, output=output)


# register_asset('require.js', 'requirejs/require.js.!')
register_asset('modernizr.js', 'modernizr/modernizr.js.!')
register_asset('jquery.js', 'jquery/dist/jquery.js.!')
# register_asset('foundation.js', 'foundation/js/foundation.js.!')
register_asset('jquery.cookie.js', 'jquery.cookie/jquery.cookie.js.!')
register_asset('jquery-placeholder.js', 'jquery-placeholder/jquery.placeholder.js.!')
register_asset('fastclick.js', 'fastclick/lib/fastclick.js.!')

register_asset('foundation.core.js', 'foundation/js/foundation/foundation.js.!')
register_asset('foundation.abide.js', 'foundation/js/foundation/foundation.abide.js.!')
register_asset('foundation.accordion.js', 'foundation/js/foundation/foundation.accordion.js.!')
register_asset('foundation.alert.js', 'foundation/js/foundation/foundation.alert.js.!')
register_asset('foundation.clearing.js', 'foundation/js/foundation/foundation.clearing.js.!')
register_asset('foundation.dropdown.js', 'foundation/js/foundation/foundation.dropdown.js.!')
register_asset('foundation.equalizer.js', 'foundation/js/foundation/foundation.equalizer.js.!')
register_asset('foundation.interchange.js', 'foundation/js/foundation/foundation.interchange.js.!')
register_asset('foundation.joyride.js', 'foundation/js/foundation/foundation.joyride.js.!')
register_asset('foundation.magellan.js', 'foundation/js/foundation/foundation.magellan.js.!')
register_asset('foundation.offcanvas.js', 'foundation/js/foundation/foundation.offcanvas.js.!')
register_asset('foundation.orbit.js', 'foundation/js/foundation/foundation.orbit.js.!')
register_asset('foundation.reveal.js', 'foundation/js/foundation/foundation.reveal.js.!')
register_asset('foundation.slider.js', 'foundation/js/foundation/foundation.slider.js.!')
register_asset('foundation.tab.js', 'foundation/js/foundation/foundation.tab.js.!')
register_asset('foundation.tooltip.js', 'foundation/js/foundation/foundation.tooltip.js.!')
register_asset('foundation.topbar.js', 'foundation/js/foundation/foundation.topbar.js.!')

# register_asset('normalize.css', 'foundation/css/normalize.css.!')
# register_asset('foundation.css', 'foundation/css/foundation.css.!')

register_asset('global.css', 'foundation/css/normalize.css.!', 'foundation/css/foundation.css.!', 'common.sass')
register_asset('global.js', 'requirejs/require.js.!', 'config.coffee', 'common.coffee')


#
# url_for
#

def url_for(endpoint, **values):
    from flask import url_for as flask_url_for
    url = flask_url_for(endpoint, **values)

    external = values.pop('_external', False)
    if external:
        return url

    if endpoint == 'static':
        url = "%s%s" % (app.config['CDN_URL_PREFIX'], url)
    return url

app.jinja_env.globals['url_for'] = url_for
