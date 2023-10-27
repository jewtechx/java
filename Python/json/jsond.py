import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

def parse_toJSON():
    return json.dumps(x, indent=4, sort_keys=True)
# def parse_toPython():
#     return json.loads(x)

xj = parse_toJSON()
# xp = parse_toPython()

print(xj)
# print(xp)