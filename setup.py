from distutils.core import setup
from setuptools import find_packages


setup(name= 'iv30atab',
      version='0.1',
     author= 'DSSS',
     author_email= 'shahroze.nabi@fau.de',
     packages= find_packages(),
     install_requires= ['numpy', 'Pillow', 'ipywidgets'])