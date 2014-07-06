requirejs.config({
  paths: {
    {% assets "jquery.js" %}'jquery': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.js" %}'foundation': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "jquery.cookie.js" %}'jquery.cookie': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "jquery-placeholder.js" %}'jquery-placeholder': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "fastclick.js" %}'fastclick': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "modernizr.js" %}'modernizr': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},

    {% assets "foundation.core.js" %}'foundation.core': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.abide.js" %}'foundation.abide': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.accordion.js" %}'foundation.accordion': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.alert.js" %}'foundation.alert': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.clearing.js" %}'foundation.clearing': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.dropdown.js" %}'foundation.dropdown': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.equalizer.js" %}'foundation.equalizer': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.interchange.js" %}'foundation.interchange': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.joyride.js" %}'foundation.joyride': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.magellan.js" %}'foundation.magellan': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.offcanvas.js" %}'foundation.offcanvas': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.orbit.js" %}'foundation.orbit': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.reveal.js" %}'foundation.reveal': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.slider.js" %}'foundation.slider': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.tab.js" %}'foundation.tab': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.tooltip.js" %}'foundation.tooltip': "{{ ASSET_URL | replace('.js','') }}"{% endassets %},
    {% assets "foundation.topbar.js" %}'foundation.topbar': "{{ ASSET_URL | replace('.js','') }}"{% endassets %}
  },
  shim: {
    'foundation': {
      deps: [
        'jquery',
        'modernizr'
      ],
      exports: 'Foundation'
    },
    'jquery.cookie': {
      deps: [
        'jquery'
      ]
    },
    'fastclick': {
      exports: 'FastClick'
    },
    'modernizr': {
      exports: 'Modernizr'
    },
    'jquery-placeholder': {
      exports: 'Placeholders'
    },

    'foundation.core': {
      deps: [
        'jquery',
        'modernizr'
      ],
      exports: 'Foundation'
    },
    'foundation.abide': { deps: ['foundation.core'] },
    'foundation.accordion': { deps: ['foundation.core'] },
    'foundation.alert': { deps: ['foundation.core'] },
    'foundation.clearing': { deps: ['foundation.core'] },
    'foundation.dropdown': { deps: ['foundation.core'] },
    'foundation.equalizer': { deps: ['foundation.core'] },
    'foundation.interchange': { deps: ['foundation.core'] },
    'foundation.joyride': { deps: ['foundation.core'] },
    'foundation.magellan': { deps: ['foundation.core'] },
    'foundation.offcanvas': { deps: ['foundation.core'] },
    'foundation.orbit': { deps: ['foundation.core'] },
    'foundation.reveal': { deps: ['foundation.core'] },
    'foundation.slider': { deps: ['foundation.core'] },
    'foundation.tab': { deps: ['foundation.core'] },
    'foundation.tooltip': { deps: ['foundation.core'] },
    'foundation.topbar': { deps: ['foundation.core'] }
  }
});
