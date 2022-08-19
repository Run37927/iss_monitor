import json

json_string = '{"first": "James", "last": "brown", "prefix": "Mr."}'

name = json.loads(json_string)

print(name['prefix'], name['first'], name['last'])
