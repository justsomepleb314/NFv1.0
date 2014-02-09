try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'name': 'NFv1.0',
    'author': 'Team NF',
    'description': '...',
    'version': '1.0',
    'install_requires': ['PRAW'],
    'packages': ['NFv1.0'],
    'scripts': []
}

setup(**config)