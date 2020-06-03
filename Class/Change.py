from datetime import datetime
from Class.Label import Label
from Class.Message import Message
from Class.Revision import Revision
from Class.Parser import Parser
import re


class Change(Parser):
    # self.created = datetime.fromisoformat(re.sub(r"\.[0-9]+", "", data['created']))
    different = {
        'number': '_number',
        'owner': 'owner/_account_id',
    }
    same = ['project', 'status', 'subject', 'created', 'updated']
    dates = ['created', 'updated']

    def parse(self):
        data = self.data
        # this handles nested and same
        result = super().parse()

        # following are for object type values ['revisions', 'reviewers', 'messages', 'labels']
        # revision
        revisions_data = data["revisions"]
        revisions = []
        for revision_id in revisions_data.keys():
            revision = Revision(revisions_data[revision_id])
            revisions.append(revision.parse())
        result['revisions'] = revisions

        # reviewers
        reviewers = []
        if "reviewers" in data.keys():
            if "REVIEWER" in data["reviewers"].keys():
                for account in data["reviewers"]["REVIEWER"]:
                    reviewers.append(account["_account_id"])
        result["reviewers"] = reviewers

        # messages
        messages_data = data["messages"]
        messages = [Message(message).parse() for message in messages_data]
        result["messages"] = messages

        # labels
        labels_data = data["labels"]
        labels = []
        for kind in labels_data.keys():
            if "all" not in labels_data[kind].keys():
                continue
            for label_data in labels_data[kind]["all"]:
                label = Label(kind, label_data)
                # 0 values aren't important
                if label.value() != 0:
                    labels.append(label.parse())
        result["labels"] = labels
        return result

    @staticmethod
    def is_mergeable(data):
        if "subject" in data.keys() and "not merge" in data["subject"].lower():
            return False
        return True
