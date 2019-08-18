# dnssec
#### A Python tool for checking a state of domains signed by dnssec

![version](https://img.shields.io/badge/version-1.0.0-brightgreen)
[![Build Status](https://travis-ci.org/patrikskrivanek/dnssec.svg?branch=master)](https://travis-ci.org/patrikskrivanek/dnssec)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/patrikskrivanek/dnssec.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/patrikskrivanek/dnssec/context:python)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

This program validates dnssec signatures in domain zones based on dns requests.
Set the domain parameter and then the program returns a message and a status code.

### Installation
```bash
# using pip
pip install dnssec

# or if you are running multiple versions of python such as 2.7.x and 3.x 
pip3 install dnssec

# from source using git clone
git clone https://github.com/patrikskrivanek/dnssec

# from source using wget
wget https://github.com/patrikskrivanek/dnssec/blob/master/dnssec
```

### Documentation
Argument | Description | Required
------------ | ------------- | -------------
--domain | Domain name for check | yes
--version | Show program version | optional
-h --help | Show program help and usage | optional

Status | Exit code | 
------------ | -------------
STATE_OK | 0
STATE_WARNING | 1
STATE_CRITICAL | 2
STATE_UNKNOWN | 3

### Examples
```bash
# check if github.com is signed by dnssec
dnssec --domain github.com

# show program help
dnssec --help

# show program version
dnssec --version
```