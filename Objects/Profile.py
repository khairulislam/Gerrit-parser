import re
from datetime import datetime

"""
{
    "registered_on": "2015-12-16 17:50:21.000000000",
    "_account_id": 1,
    "name": "dandy potas",
    "email": "dandypotas@gmail.com",
    "secondary_emails": [],
    "username": "dandy-p"
}
"""


class Profile:
    account_id = ''
    registered_on = ''

    def __init__(self, data):
        self.account_id = data["_account_id"]
        date = re.sub(r"\.[0-9]+", "", data["registered_on"])
        self.registered_on = datetime.fromisoformat(date)
