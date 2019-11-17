from Objects import Parser


class ChangeSummary(Parser):
    different = {'number': '_number'}
    same = ['project', 'created', 'updated', 'status']
    dates = ['created', 'updated']


class ProfileDetails(Parser):
    def __init__(self, account_id, data):
        super().__init__(data)
        self.account_id = account_id

    def parse(self):
        result = super().parse()
        result['account_id'] = self.account_id
        result['change_summaries'] = [ChangeSummary(change).parse() for change in self.data]
        return result
