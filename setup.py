try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'NBIS works website and API',
    'version': '3.0',
    'install_requires': [
        'flask==1.0.2',
        'flask-restplus==0.12.1',
        'requests==2.21.0',
        'gevent==1.4.0',
        'cryptography==2.6.1'
    ],
    'scripts': [],
    'name': 'doi-bils'
}

setup(**config)
