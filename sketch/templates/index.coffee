require ['{% assets "config.js" %}{{ASSET_URL}}{% endassets %}'], ->
  require [
    'jquery'
    'modernizr'
    'fastclick'
    'foundation.reveal'
  ], ->
    $(document).foundation({})
    $('#myModal').foundation('reveal', 'open')
