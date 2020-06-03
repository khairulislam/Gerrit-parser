from Class.Parser import Parser

"""
{
    "id": "bfdaf3ff_394d0f9a",
    "author": {
        "_account_id": 13039
    },
    "date": "2019-01-16 14:18:15.000000000",
    "message": "Patch Set 1: Code-Review+2",
    "_revision_number": 1
}
"""


class Message(Parser):
    different = {'revision_number': '_revision_number'}
    same = ['date', 'message']
    dates = ['date']

    def parse(self):
        result = super().parse()

        data = self.data
        if 'real_author' in data.keys():
            result['author'] = data['real_author']['_account_id']
        elif 'author' in data.keys():
            result['author'] = data['author']['_account_id']
        return result
