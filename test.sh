#!/bin/bash

set -eux

mypy xmod
isort xmod test
black xmod test
ruff check --fix xmod test
coverage run $(which pytest)
coverage html
