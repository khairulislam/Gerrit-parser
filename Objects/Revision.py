from Objects.File import File
from Objects.Parser import Parser

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


class Revision(Parser):
    different = {'number': '_number', 'uploader': 'uploader/_account_id'}
    same = ['created']
    dates = ['created']

    def parse(self):
        result = super().parse()

        data = self.data
        result['files'] = [File(data['files'][file_name], file_name, ).parse() for file_name in data['files'].keys()]
        return result
