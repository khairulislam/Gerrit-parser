from Class.Parser import Parser

"""
"bin/ovb-instack": {
    "lines_inserted": 1,
    "lines_deleted": 1,
    "size_delta": 7,
    "size": 3640
}
"""


class File(Parser):
    same = ['lines_deleted', 'lines_inserted', 'size', 'size_delta', 'status']

    def __init__(self, data, name):
        super().__init__(data)
        self.name = name

    def parse(self):
        result = super().parse()
        result['name'] = self.name
        return result

