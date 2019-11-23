from datetime import datetime
import re


class Parser:
    # for which key and path are different
    different = {}
    # for which key and path are same
    same = []
    #  specify date keys again in this array
    dates = []

    def __init__(self, data):
        self.data = data

    def parse(self):
        data = self.data
        result = {}
        for same_key in self.same:
            if same_key in data.keys():
                result[same_key] = data[same_key]
            else:
                result[same_key] = ''

        for different_key in self.different:
            different_result = self.get(data, path=self.different[different_key])
            if different_result is not None:
                result[different_key] = different_result
            else:
                # print("{0} not in path".format(different_key))
                result[different_key] = ''
        
        # remove microseconds from dates
        for date_key in self.dates:
            if date_key in result.keys():
                result[date_key] = self.fix_date(result[date_key])

        return result

    def get(self, data, path):
        paths = path.split("/")

        for path in paths:
            if type(data) == dict:
                if path in data.keys():
                    data = data[path]
                else:
                    # print("Couldn't find {0} in {1}".format(path, data))
                    return None
            else:
                print("Not dict type")
                return None

        return data

    def fix_date(self, date):
        # return datetime.fromisoformat(re.sub(r"\.[0-9]+", "", date))
        return re.sub(r"\.[0-9]+", "", date)

