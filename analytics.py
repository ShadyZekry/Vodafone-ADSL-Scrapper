#!/usr/bin/env python
import sys
import json
from datetime import datetime

resultJson = json.loads(sys.argv[1])

usageString = resultJson[0]["bucket"][0]["bucketCounter"][0]["value"]["amount"]
validForString = resultJson[0]["bucket"][0]["bucketBalance"][0]["validFor"]["endDateTime"].split('T')[0]
remainingString = resultJson[0]["bucket"][0]["bucketBalance"][0]["remainingValue"]["amount"]

#Main data fetched
usage = int(usageString) / 1024
remaining = int(remainingString) / 1024
expirationDate = datetime.strptime(validForString, '%Y-%m-%d')

#Helper data
remainingDays = (expirationDate - datetime.now()).days
daysPast = (datetime.now() - expirationDate.replace(month= expirationDate.month-1)).days
averageDailyUsage = usage/daysPast

print("Used GBs:\t\t%.2f" % usage, "GBs")
print("Remaining GBs:\t\t%.2f" % remaining, "GBs")
print("Expiration date:\t", expirationDate.strftime('%Y-%m-%d'))
print("Days left:\t\t", remainingDays, "Day(s)")
print("Days past:\t\t", daysPast, "Day(s)")
print("Average daily usage:\t%.2f" % averageDailyUsage, "GBs/Day")
