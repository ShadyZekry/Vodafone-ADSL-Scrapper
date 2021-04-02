import json

result = '[{"bucket":[{"usageType":"DATA","bucketBalance":[{"remainingValue":{"amount":25293.0,"units":"MB"},"validFor":{"endDateTime":"2021-04-18T00:00:00.000+0000"},"@type":"Remaining"}],"bucketCounter":[{"value":{"amount":153907.0,"units":"MB"},"@type":"Used"}],"product":[{"name":"ADSL_Mc_HS_30M_175G_Main","@baseType":"Active"}]}],"@type":"DATA"}]'

resultJson = json.loads(result)

usage = resultJson[0]["bucket"][0]["bucketBalance"][0]["remainingValue"]
validFor = resultJson[0]["bucket"][0]["bucketBalance"][0]["validFor"]
remaining = resultJson[0]["bucket"][0]["bucketCounter"][0]["value"]

print(usage)
print(validFor)
print(remaining)
