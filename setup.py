from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = 'v1.0'
DESCRIPTION = 'Natural Language Processing Model'
LONG_DESCRIPTION = '-'

# Setting up
setup(
    name="LangPy",
    version=VERSION,
    author="Mitchell Shibilski-Unkel",
    author_email="None",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['nltk', 'translate'],
    keywords=['python', 'nlp', 'translate', "polish", "english"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)