from datetime import datetime
import re
"""
"Verified": {
    "all": [
        {
            "value": 2,
            "date": "2019-01-16 13:37:34.000000000",
            "_account_id": 24072
        },
    ],
    "values": {
        "-2": "Fails",
        "-1": "Doesn't seem to work",
        " 0": "No score",
        "+1": "Works for me",
        "+2": "Verified"
    },
    "default_value": 0
},
"""


class Label:
    kind = ''
    value = ''
    date = ''
    account_id = ''

    def __init__(self, kind, data):
        self.kind = kind
        if "value" in data.keys():
            self.value = data["value"]
        if "date" in data.keys():
            self.date = datetime.fromisoformat(re.sub(r"\.[0-9]+", "", data['date']))
        self.account_id = data["_account_id"]
