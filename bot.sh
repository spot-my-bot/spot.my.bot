#!/bin/bash
set -e
dist=spot.my.bot
mkdir $dist || true
#pip install -r requirements.txt --target $dist
PYTHONPATH=$dist python bot.py
