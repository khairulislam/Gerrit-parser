import json
from Objects.Change import Change
import pandas as pd
import csv
from os import listdir
from os.path import isfile, join

header = ['project', 'subject', 'created', 'updated', 'number', 'owner', 'reviewers', 'revisions',
          'messages', 'labels', 'status']
initialize = True


def filter_features(dict):
    features = []
    for col in header:
        if col in dict.keys():
            features.append(dict[col])
        else:
            features.append('')
    return features


root = ""
for year in range(2013, 2019):
    path = root + "\\eclipse {0}".format(year)
    onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

    output_file_name = root + "\\eclipse_features_{0}.csv".format(year)
    if initialize:
        print("Initializing ...")
        with open(output_file_name, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', dialect='excel')
            writer.writerow(header)
            csvfile.close()

    output_file = open(output_file_name, "a", newline='', encoding="utf-8")
    output_writer = csv.writer(output_file, dialect='excel')

    all_values = []
    for input_file_name in onlyfiles:
        with open(input_file_name) as file:
            print(input_file_name + " loading..", end='')
            changes = json.load(file)
            for json_data in changes:
                change = Change(json_data)
                parsed = change.parse()

                values = filter_features(parsed)
                output_writer.writerow(values)
                all_values.append(values)
            # need to do this to reduce memory
            output_file.flush()
            print(" done")

    output_file.close()
