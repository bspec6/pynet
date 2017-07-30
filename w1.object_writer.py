#!/usr/bin/env python
import yaml
import json
import pprint

some_list = range(6)
some_list.append('thingOne')
some_list.append('thingTwo')
some_list.append({})
some_list[-1]['ipaddr'] = '10.1.1.1'

with open("w1.file.yml", "w") as f:
	f.write(yaml.dump(some_list, default_flow_style=False))

with open("w1.file.json", "w") as g:
	json.dump(some_list, g)
