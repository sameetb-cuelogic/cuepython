
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	"description": "PROJECT DESCRIPTION",
	"author": "AUTHOR NAME",
	"url": "GET URL",
	"download_url": "DOWNLOAD URL",
	"author_email": "AUTHOR EMAIL",
	"version": "0.0",
	"install_requires": ["nose"],
	"packages": ["NAME"],
	"scripts": [],
	"name": "PROJECT NAME"
}

setup(**config)
