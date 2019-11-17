import json
from Objects.Change import Change
import pandas as pd

with open("data/change.json") as file:
    changes = json.load(file)
    for json in changes:
        change = Change(json)
        parsed = change.parse()
        columns = [x for x in parsed.keys()]
        values = [x for x in parsed.values()]
        print(columns)
        print(values)
        df = pd.DataFrame([values], columns=columns)
        df.to_csv('sample.csv', index=False)
        break
