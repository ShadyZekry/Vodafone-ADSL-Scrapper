# !/bin/sh
# result=$(node puppeteer/index.js) &&

# python analytics.py "$result"

result=`
 cat input.txt | tee >(awk '{
        if($1 == "\"log\""){
            $1 = "";
            print $0
        }
    }' > /dev/tty) | awk '{if($1 != "\"log\"") print $0;}'
    `

echo "result is"
echo $result
