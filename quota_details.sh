# !/bin/sh
result=$(node puppeteer/index.js) &&

python analytics.py "$result"