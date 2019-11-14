"""
"bin/ovb-instack": {
    "lines_inserted": 1,
    "lines_deleted": 1,
    "size_delta": 7,
    "size": 3640
}
"""


class File:
    file_name = ''
    status = ''
    lines_inserted = 0
    lines_deleted = 0
    size_delta = 0
    size = 0

    def __init__(self, name, data):
        self.file_name = name

        if "lines_deleted" in data.keys():
            self.lines_deleted = data['lines_deleted']
        if "lines_inserted" in data.keys():
            self.lines_inserted = data['lines_inserted']
        self.size = data['size']
        self.size_delta = data['size_delta']
        if 'status' in data.keys():
            self.status = data['status']