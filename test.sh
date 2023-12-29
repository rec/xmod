#!/bin/bash

set -eux

mypy xmod.py
isort xmod.py test
black xmod.py test
ruff check --fix xmod.py test
coverage run $(which pytest)
coverage html
