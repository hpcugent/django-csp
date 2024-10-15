# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['csp', 'csp.contrib', 'csp.extensions', 'csp.templatetags', 'csp.tests']

package_data = \
{'': ['*']}

install_requires = \
['django>=4.2']

setup_kwargs = {
    'name': 'django-csp',
    'version': '4.0b2',
    'description': 'Django Content Security Policy support.',
    'long_description': '.. image:: https://badge.fury.io/py/django-csp.svg\n   :target: https://pypi.python.org/pypi/django_csp\n\n.. image:: https://github.com/mozilla/django-csp/actions/workflows/ci.yaml/badge.svg\n   :target: https://github.com/mozilla/django-csp/actions/workflows/ci.yaml\n\n==========\nDjango-CSP\n==========\n\nDjango-CSP adds Content-Security-Policy_ headers to Django.\n\nThe code lives on GitHub_, where you can report Issues_.\n\nThe full documentation is available on ReadTheDocs_.\n\n.. _Content-Security-Policy: http://www.w3.org/TR/CSP/\n.. _GitHub: https://github.com/mozilla/django-csp\n.. _Issues: https://github.com/mozilla/django-csp/issues\n.. _ReadTheDocs: http://django-csp.readthedocs.org/\n',
    'author': 'James Socol',
    'author_email': 'me@jamessocol.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
