from Class.Parser import Parser
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


class Profile(Parser):
    different = {'account_id': '_account_id'}
    same = ['registered_on']
    dates = ['registered_on']
