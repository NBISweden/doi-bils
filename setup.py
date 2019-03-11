try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'doi-bils',
    'version': '1.3',
    'install_requires': [
        'flask==1.0.2',
        'flask-restplus==0.12.1',
        'PyYAML>=3.13'
    ],
    'scripts': [],
    'name': 'doi-bils'
}

setup(**config)
