#!/usr/bin/env python3

import csv
import random
import glob
import sys
import yaml

TAS      = [ta['github'] for ta in yaml.safe_load(open('static/yaml/ta.yaml'))]
STUDENTS = []

for student in csv.DictReader(open('static/csv/students.csv', 'r')):
    STUDENTS.append(student['Netid'])

CONFLICTS = {
    ta['github']: ta['conflicts']
    for ta in yaml.safe_load(open('static/yaml/ta.yaml'))
    if ta.get('conflicts')
}

has_conflict = True

while has_conflict:
    random.shuffle(STUDENTS)
    random.shuffle(TAS)

    TAS          = TAS * (len(STUDENTS) // len(TAS) + 1)
    MAPPING      = sorted(map(list, zip(STUDENTS, TAS)))
    has_conflict = False

    for ta, conflicts in CONFLICTS.items():
        for conflict in conflicts:
            if [conflict, ta] in MAPPING:
                has_conflict = True

print(yaml.dump(MAPPING, default_flow_style=False))
