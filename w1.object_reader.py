#!/usr/bin/env python

from pprint import pprint
import yaml
import json

with open("w1.file.yml") as f:
	read_in_yaml = yaml.load(f)

with open("w1.file.json") as g:
	read_in_json = json.load(g)

pprint(read_in_yaml)
pprint(read_in_json)
