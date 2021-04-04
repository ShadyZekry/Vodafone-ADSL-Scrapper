# !/bin/sh
# result=$(node puppeteer/index.js) &&

# python analytics.py "$result"

result=$(echo '"log" Logging in ...' | awk '{
    print $0
    if($0 == "\"log\"") print "\"log\""
    }' > /dev/tty)
echo "result is"
echo $result