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

webassets.url = '%s/assets' % app.static_url_path
webassets.append_path(os.path.abspath('%s/../templates' % app.static_folder))
webassets.append_path(os.path.abspath('%s/../bower_components' % app.static_folder))
# webassets.append_path(app.static_folder)

if webassets.config.get('directory'):
    app.logger.info("assets.directory: %s" % webassets.directory)
else:
    import tempfile
    webassets.directory = tempfile.mkdtemp()
    app.logger.warn("assets.directory: %s" % webassets.directory)


#
# register global assets
#

@app.route('%s/assets/<path:filename>' % app.static_url_path, endpoint='assets')
def _send_assets_file(filename):
    cache_timeout = app.get_send_file_max_age(filename)
    return flask.helpers.send_from_directory(
        webassets.directory, filename, cache_timeout=cache_timeout)

def register_asset(name, *asset_files):
    if not asset_files:
        asset_files = [name]
    bundles = []
    for asset_file in asset_files:
        _, fe = os.path.splitext(asset_file)
        if fe == '.js':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=('jinja2', 'uglifyjs')
            )
        elif fe == '.coffee':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=('jinja2', 'coffeescript', 'uglifyjs')
            )
        elif fe == '.css':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=('jinja2', 'cssmin')
            )
        elif fe == '.sass':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file, '**/*.sass', '*.sass'],
                filters=('compass', 'cssmin')
            )
        elif fe == '.scss':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file, '**/*.scss', '*.scss'],
                filters=('compass', 'cssmin')
            )
        else:
            raise ValueError('%s not support', asset_file)
        bundles.append(bundle)

    fn, fe = os.path.splitext(name)
    output = '%s.%%(version)s%s' % (fn, fe)
    webassets.register(name, *bundles, output=output)


def register_bower_component(name, *asset_files):
    if not asset_files:
        asset_files = [name]
    bundles = []
    for asset_file in asset_files:
        _, fe = os.path.splitext(asset_file)
        if fe == '.js':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=('uglifyjs')
            )
        elif fe == '.coffee':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=('coffeescript', 'uglifyjs')
            )
        elif fe == '.css':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file],
                filters=('cssmin')
            )
        elif fe == '.sass':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file, '**/*.sass', '*.sass'],
                filters=('compass', 'cssmin')
            )
        elif fe == '.scss':
            bundle = flask.ext.assets.Bundle(
                asset_file, depends=[asset_file, '**/*.scss', '*.scss'],
                filters=('compass', 'cssmin')
            )
        else:
            raise ValueError('%s not support', asset_file)
        bundles.append(bundle)

    fn, fe = os.path.splitext(name)
    output = '%s.%%(version)s%s' % (fn, fe)
    webassets.register(name, *bundles, output=output)


register_bower_component('require.js', 'requirejs/require.js')
register_bower_component('modernizr.js', 'modernizr/modernizr.js')
register_bower_component('jquery.js', 'jquery/dist/jquery.js')
register_bower_component('foundation.js', 'foundation/js/foundation.js')
register_bower_component('jquery.cookie.js', 'jquery.cookie/jquery.cookie.js')
register_bower_component('jquery-placeholder.js', 'jquery-placeholder/jquery.placeholder.js')
register_bower_component('fastclick.js', 'fastclick/lib/fastclick.js')

register_bower_component('foundation.core.js', 'foundation/js/foundation/foundation.js')
register_bower_component('foundation.abide.js', 'foundation/js/foundation/foundation.abide.js')
register_bower_component('foundation.accordion.js', 'foundation/js/foundation/foundation.accordion.js')
register_bower_component('foundation.alert.js', 'foundation/js/foundation/foundation.alert.js')
register_bower_component('foundation.clearing.js', 'foundation/js/foundation/foundation.clearing.js')
register_bower_component('foundation.dropdown.js', 'foundation/js/foundation/foundation.dropdown.js')
register_bower_component('foundation.equalizer.js', 'foundation/js/foundation/foundation.equalizer.js')
register_bower_component('foundation.interchange.js', 'foundation/js/foundation/foundation.interchange.js')
register_bower_component('foundation.joyride.js', 'foundation/js/foundation/foundation.joyride.js')
register_bower_component('foundation.magellan.js', 'foundation/js/foundation/foundation.magellan.js')
register_bower_component('foundation.offcanvas.js', 'foundation/js/foundation/foundation.offcanvas.js')
register_bower_component('foundation.orbit.js', 'foundation/js/foundation/foundation.orbit.js')
register_bower_component('foundation.reveal.js', 'foundation/js/foundation/foundation.reveal.js')
register_bower_component('foundation.slider.js', 'foundation/js/foundation/foundation.slider.js')
register_bower_component('foundation.tab.js', 'foundation/js/foundation/foundation.tab.js')
register_bower_component('foundation.tooltip.js', 'foundation/js/foundation/foundation.tooltip.js')
register_bower_component('foundation.topbar.js', 'foundation/js/foundation/foundation.topbar.js')

register_bower_component('normalize.css', 'foundation/css/normalize.css')
register_bower_component('foundation.css', 'foundation/css/foundation.css')

register_asset('common.css', 'common.sass')
register_asset('config.js')
