#!/usr/bin/env bash
[[ -d ./venv ]] || mkdir ./venv
virtualenv ./venv
. venv/bin/activate
pip install -r requirements.txt
python ./scraper.py
