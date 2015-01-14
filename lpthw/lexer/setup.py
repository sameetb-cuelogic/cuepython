
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	"description": "Game Lexicon",
	"author": "CueLogic",
	"url": "GET URL",
	"download_url": "DOWNLOAD URL",
	"author_email": "AUTHOR EMAIL",
	"version": "0.0",
	"install_requires": ["nose"],
	"packages": ["lexer"],
	"scripts": [],
	"name": "Game Lexicon"
}

setup(**config)
