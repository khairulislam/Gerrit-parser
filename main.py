import json, re
from Objects.Change import Change


with open("data/change.json") as file:
    changes = json.load(file)
    for json in changes:
        change = Change(json)
        print(change.updated - change.created)
