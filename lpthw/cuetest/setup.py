
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	"description": "Python Test",
	"author": "CueLogic",
	"url": "GET URL",
	"download_url": "DOWNLOAD URL",
	"author_email": "AUTHOR EMAIL",
	"version": "0.0",
	"install_requires": ["nose"],
	"packages": ["cuetest"],
	"scripts": [],
	"name": "CueTest"
}

setup(**config)
