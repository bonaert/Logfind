try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'logfind',
    'author': 'harokb',
    'author_email': 'harokb@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)
