import json, re
from Objects.Change import Change

with open("data/change.json") as file:
    changes = json.load(file)
    for json in changes:
        change = Change(json)


# convert any json to struct. However in our work, we want to fully control this process
# so won't use this class
class Struct(dict):
    def __init__(self, data):
        super().__init__(data)
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value

    def __repr__(self):
        return '{%s}' % str(',\n '.join("'%s':\n %s" % (k, repr(v)) for (k, v) in self.__dict__.items()))