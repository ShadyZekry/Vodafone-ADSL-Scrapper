# Vodafone-ADSL-Scrapper
Fetch general info about the remaining quota details with headless browsing.

Using Puppeteer, that uses NodeJS

## Prerequisites
* Bash
<br>

* Python

<br>

* NPM
<br>

* Node
<br>

You need to initialize nodejs in your project before adding the puppeteer direcrtory, to create the `node_modules` folder.
```
$ npm init
```

## Output Example
```
Used GBs:		26.33 GBs (15.0%)
Remaining GBs:		148.67 GBs (85.0%)
Expiration date:	 2021-04-18
Days left:		 10 Day(s)
Days past:		 20 Day(s)
Average daily usage:	1.32 GBs/Day
```

## Notes
* Before using the script,you need to enter your phone & password manually in /puppeteer/index.js

* Any unexpected behavior is not handeled "yet", like invalid phone/pass, or internet issues, or any unxpected routing of the website
 but don't worry, you will know the issue from the logs.
