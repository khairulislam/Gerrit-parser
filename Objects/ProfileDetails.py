from datetime import datetime
import re


class ChangeSummary:
    change_number = ''
    project = ''
    topic = ''
    created = ''
    updated = ''
    status = ''

    def __init__(self, data):
        self.change_number = data["_number"]
        self.project = data["project"]
        self.subject = data['subject'].replace('\'', '')
        if 'topic' in data.keys():
            self.topic = data['topic'].replace('\'', '')
        self.created = datetime.fromisoformat(re.sub(r"\.[0-9]+", "", data['created']))
        self.status = data['status']


class ProfileDetails:
    account_id = ''
    changeSummaries: [ChangeSummary] = []

    def __init__(self, account_id, data):
        self.account_id = account_id
        self.changeSummaries = [ChangeSummary(change) for change in data]
