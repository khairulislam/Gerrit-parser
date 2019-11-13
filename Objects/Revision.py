from datetime import datetime
from Objects.File import *
import re

"""
"revisions": {
    "53ea11205f100d59130f75697cd55f70b1276911": {
        "kind": "REWORK",
        "_number": 1,
        "created": "2019-01-16 13:37:09.000000000",
        "uploader": {
            "_account_id": 2276
        },
        "ref": "refs/changes/20/631220/1",
        "fetch": {
            "git": {
                "url": "git://git.openstack.org/openstack/kolla",
                "ref": "refs/changes/20/631220/1"
            },
            "anonymous http": {
                "url": "https://git.openstack.org/openstack/kolla",
                "ref": "refs/changes/20/631220/1"
            }
        },
        "files": {
            "docker/base/Dockerfile.j2": {
                "lines_inserted": 1,
                "lines_deleted": 1,
                "size_delta": 9,
                "size": 16408
            }
        }
    }
}
"""


class Revision:
    id = ''
    number = ''
    created = ''
    files: [File] = []

    def __init__(self, id, data):
        self.id = id
        self.number = data['_number']
        self.created = re.sub(".[0-9]+0000", "", data['created'])
        self.files = [File(file_name, data["files"][file_name]) for file_name in data["files"].keys()]