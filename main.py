import json
from Objects.Change import Change
import pandas as pd
import csv
from os import listdir
from os.path import isfile, join

path = "eclipse 2009"
onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)


initialize = True
header = ['project', 'subject', 'created', 'updated', 'number', 'owner', 'reviewers', 'revisions',
          'messages', 'labels', 'status']

output_file_name = "eclipse_features.csv"
if initialize:
    print("Initializing ...")
    with open(output_file_name, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', dialect='excel')
        writer.writerow(header)
        csvfile.close()

output_file = open(output_file_name, "a", newline='')
output_writer = csv.writer(output_file, dialect='excel')


def filter_features(dict):
    features = []
    for col in header:
        if col in dict.keys():
            features.append(dict[col])
        else:
            features.append('')
    return features


for input_file_name in onlyfiles:
    with open(input_file_name) as file:
        print(input_file_name + " loading..")
        changes = json.load(file)
        for json_data in changes:
            change = Change(json_data)
            parsed = change.parse()

            values = filter_features(parsed)
            output_writer.writerow(values)
        # need to do this to reduce memory
        output_file.flush()
        print(input_file_name + " done")
output_file.close()
