# Introduction

This repository provides an environment to build then publish automatically Lambda@Edge functions. It provides:

* Node 6 (mandatory for Lambda@Edge)
* Python 3 environment. 

There are also some tool packages installed like:

* [yasha](https://github.com/kblomqvist/yasha)
* [yq](https://pypi.python.org/pypi/yq/2.3.0)
* boto3 libraries
* AWS cli

And some Python scripts (in /base/scripts) to publish lambda versions to AWS.

# Docker build

This repository is automatically built using Docker Hub.

# How to use

You can base your own images directly on this. It doesn't provide any building logic, just the building environment as tool and the publish scripts.
