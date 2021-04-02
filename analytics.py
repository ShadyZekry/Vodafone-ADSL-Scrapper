import json
import datetime

result = '[{"bucket":[{"usageType":"DATA","bucketBalance":[{"remainingValue":{"amount":25293.0,"units":"MB"},"validFor":{"endDateTime":"2021-04-18T00:00:00.000+0000"},"@type":"Remaining"}],"bucketCounter":[{"value":{"amount":153907.0,"units":"MB"},"@type":"Used"}],"product":[{"name":"ADSL_Mc_HS_30M_175G_Main","@baseType":"Active"}]}],"@type":"DATA"}]'

resultJson = json.loads(result)

usageString = resultJson[0]["bucket"][0]["bucketBalance"][0]["remainingValue"]["amount"]
validForString = resultJson[0]["bucket"][0]["bucketBalance"][0]["validFor"]["endDateTime"].split('T')[0]
remainingString = resultJson[0]["bucket"][0]["bucketCounter"][0]["value"]["amount"]

#expirationDate = datetime.datetime.strptime(validForString, '%Y-%m-%d %H:%M:%S.%f')
#expirationDate = datetime.datetime.strptime(validForString, 'YYYY-MM-DDThh:mm:ss.sTZD')
expirationDate = datetime.datetime.strptime(validForString, '%Y-%M-%d')

print(int(usageString))
print(expirationDate)
print(int(remainingString))
