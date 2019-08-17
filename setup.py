from setuptools import setup
import codecs

with codecs.open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name="dnssec",
    version="v0.0.0",
    url="https://github.com/patrikskrivanek/dnssec",
    download_url="https://github.com/patrikskrivanek/dnssec/releases",
    author="Patrik Skřivánek",
    author_email="kriegsmarine1995@gmail.com",
    description="A Python tool for checking a state of domains signed by dnssec",
    long_description=readme,
    keywords="dnssec validation",
    python_requires=">=3.6",
    packages=["dnssec"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)