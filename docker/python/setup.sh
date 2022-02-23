#!/bin/bash
set -eu
cd /var/app/python/src
poetry install
poetry run alembic upgrade head
python3
