import json

raw_json = """{
"a":"aa",
"b":"bb",
"c":"cc",
"d":true,
"e":false,
"f":null
}"""


print(type(raw_json))
print(raw_json)

python_struct = json.loads(raw_json)
print(type(python_struct))
print(type(python_struct["d"]))
print(python_struct)

json_again = json.dumps(raw_json)
print(type(json_again))
print(json_again)
