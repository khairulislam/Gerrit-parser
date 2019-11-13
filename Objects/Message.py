from datetime import datetime
import re

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


class Message:
    id = ''
    author_id = ''
    date = ''
    message = ''
    revision_no = 0

    def __init__(self, data):
        # message.message = msg['message'].replace('\'', '')
        self.id = data['id']
        self.message = data['message']

        if '_revision_number' in data.keys():
            self.revision_no = data['_revision_number']

        if 'date' in data.keys():
            self.date = datetime.fromisoformat(re.sub(r"\.[0-9]+", "", data['date']))

        if 'real_author' in data.keys():
            self.author_id = data['real_author']['_account_id']
        elif 'author' in data.keys():
            self.author_id = data['author']['_account_id']