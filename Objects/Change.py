from datetime import datetime
from Objects.Label import Label
from Objects.Message import Message
from Objects.Revision import Revision
import re


class Change:
    change_number = ''
    author_id = ''
    subject = ''

    topic = ''
    created = ''
    deletions = 0

    insertions = 0
    updated = ''
    project = ''

    status = ''

    revisions: [Revision] = []
    reviewers: [str] = []
    messages: [Message] = []
    labels: [Label] = []

    def __init__(self, data):
        self.change_number = data['_number']

        self.author_id = data['owner']['_account_id']
        self.subject = data['subject'].replace('\'', '')
        if 'topic' in data.keys():
            self.topic = data['topic'].replace('\'', '')
        self.created = datetime.fromisoformat(re.sub(r"\.[0-9]+", "", data['created']))

        if "deletions" in data.keys():
            self.deletions = data['deletions']
        if "insertions" in data.keys():
            self.insertions = data['insertions']

        self.updated = datetime.fromisoformat(re.sub(r"\.[0-9]+", "", data['updated']))
        self.project = data['project']
        self.status = data['status']

        revisions = data["revisions"]
        self.revisions = []
        for revision_id in revisions.keys():
            self.revisions.append(Revision(revision_id, revisions[revision_id]))

        if "reviewers" in data.keys():
            if "REVIEWER" in data["reviewers"].keys():
                for account in data["reviewers"]["REVIEWER"]:
                    self.reviewers.append(account["_account_id"])

        messages = data["messages"]
        self.messages = [Message(messageBody) for messageBody in messages]
        labels = data["labels"]
        for kind in labels.keys():
            for label in labels[kind]["all"]:
                self.labels.append(Label(kind, label))

    @staticmethod
    def is_mergeable(data):
        if "subject" in data.keys() and "not merge" in data["subject"].lower():
            return False
        return True
