#!/usr/bin/env bash
[[ -d /tmp/venv ]] || mkdir /tmp/venv
virtualenv /tmp/venv
. /tmp/venv/bin/activate
pip install -r requirements.txt
pip install pytest
pytest
