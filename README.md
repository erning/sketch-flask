# Sketch Flask

## Quick start

fetch code

```
$ git clone git@github.com:erning/sketch-flask.git
$ cd sketch-flask
```

provision the dev vm

```
$ vagrant up
$ vagrant provision
$ vagrant ssh
```

start webapp in vm

```
$ cd /vagrant
$ bower install
$ sudo pip install -f requirements.txt
$ honch start
```

open the url http://127.0.0.1:5000/

## Stack

- [Flask](http://flask.pocoo.org/)
- [WebAssets](http://webassets.readthedocs.org/)
- [RequireJS](http://requirejs.org/)
- [Foundation](http://foundation.zurb.com/r)
