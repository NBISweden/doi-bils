try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'NBIS works website and API',
    'version': '1.7',
    'install_requires': [
        'flask==1.0.2',
        'flask-restplus==0.12.1',
        'requests==2.21.0'
    ],
    'scripts': [],
    'name': 'doi-bils'
}

setup(**config)
