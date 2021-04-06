# !/bin/bash
result=`
 node puppeteer/index.js | tee >(awk '{
        if($1 == "\"log\""){
            $1 = "";
            print $0
        }
    }' > /dev/tty) | awk '{if($1 != "\"log\"") print $0;}'
    ` &&

python analytics.py "$result"
