import json
import os
from Class.Change import Change
from pprint import PrettyPrinter

data_root = "Data"
filepath = os.path.join(data_root, "changes.json")

pprint = PrettyPrinter(indent=1)

with open(filepath) as file:
    change_json = json.load(file)[0]  # loading the first change json of the dumped response list
    parsed_change = Change(change_json).parse()
    pprint.pprint(parsed_change)