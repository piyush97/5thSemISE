import json

# some JSON:
x = '{ "name":"Piyush", "age":20, "city":"New Delhi"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
