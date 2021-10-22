# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['django_non_dark_admin', 'django_non_dark_admin.templatetags']

package_data = \
{'': ['*'],
 'django_non_dark_admin': ['static/django_non_dark_admin/*',
                           'templates/admin/*',
                           'templates/django_non_dark_admin/*']}

install_requires = \
['django>=3.2']

setup_kwargs = {
    'name': 'django-non-dark-admin',
    'version': '1.0',
    'description': 'Disable dark mode in Django admin user interface in Django 3.2.x.',
    'long_description': "Django Non Dark Admin\n=====================\n\nDisable or enable dark mode user interface in Django admin panel (Django==3.2).\n\nInstallation\n------------\nFor install this app run in terminal:\n::\n\n    pip install django-non-dark-admin\n\nConfiguration\n-------------\nAdd ''django_non_dark_admin'' to your ``INSTALLED_APPS`` settings. This is must be added **BEFORE** ''django.contrib.admin''.\n\nSet ''DISABLE_DARK_MODE = True'' in your settings module to diable dark mode in admin panel user interface.\n\nLicense\n-------\nLicensed under BSD license. See `license link`_ in documentation.\n\n.. _license link: LICENSE.rst",
    'author': 'Artem Galichkin',
    'author_email': 'doomer3d@gmail.com',
    'maintainer': 'Artem Galichkin',
    'maintainer_email': 'doomer3d@gmail.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
