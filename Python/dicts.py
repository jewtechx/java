executives = [
     {"name":"Jew", "position":"C.E.O", "salary":"$217,000"},
    {"name":"Kelvin", "position":"Lead Developer", "salary":"$207,000"},
    {"name":"Elclif", "position":"Hardware Engineer", "salary":"$211,000"},
    {"name":"Fransic", "position":"Graphic Designer", "salary":"$200,000"},
]

for dev in executives:
    print(f"{dev["name"]} is the {dev["position"]}. He takes {dev["salary"]}",sep="\n")