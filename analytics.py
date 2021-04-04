#!/usr/bin/env python
import sys
import json
import datetime

resultJson = json.loads(sys.argv[1])

usageString = resultJson[0]["bucket"][0]["bucketBalance"][0]["remainingValue"]["amount"]
validForString = resultJson[0]["bucket"][0]["bucketBalance"][0]["validFor"]["endDateTime"].split('T')[0]
remainingString = resultJson[0]["bucket"][0]["bucketCounter"][0]["value"]["amount"]

#expirationDate = datetime.datetime.strptime(validForString, '%Y-%m-%d %H:%M:%S.%f')
#expirationDate = datetime.datetime.strptime(validForString, 'YYYY-MM-DDThh:mm:ss.sTZD')
expirationDate = datetime.datetime.strptime(validForString, '%Y-%M-%d')

print(int(usageString))
print(expirationDate)
print(int(remainingString))
