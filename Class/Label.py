from Class.Parser import Parser

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


class Label(Parser):
    different = {'account_id': '_account_id'}
    same = ['date']
    dates = ['date']

    def __init__(self, kind, data):
        super().__init__(data)
        self.kind = kind

    def parse(self):
        result = super().parse()
        result['kind'] = self.kind
        result['value'] = self.value()
        return result

    def value(self):
        if 'value' in self.data.keys():
            return self.data['value']
        return 0
