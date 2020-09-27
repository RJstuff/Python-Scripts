import json

#names = json.loads(open("surnames.json").read())

with open('surnames.json') as json_data:
    data = json.load(json_data)
