#!/usr/bin/python

import json

DOCUMENTATION = '''
---
module: get_time
short_description: Get time based on IP address
'''

EXAMPLES = '''
- name: Get time
  get_time:
    ipaddress : "10.0.0.1"
  register: time
'''

from ansible.module_utils.basic import *


def ip_time_min(data):
    valueip = data.split(".")
    minimalip = "".join(valueip[2:4])
    minutes = int(minimalip) % 60
    return minutes


def ip_time_hour(data):

    valueip = data.split(".")
    minimalip = "".join(valueip[2:4])
    hour = int(minimalip) % 24
    return hour


def main():

    module = AnsibleModule(
        argument_spec = dict(
            ipaddress = dict(required=True, type="str"),
        )
    )

    ipaddress = module.params['ipaddress']
    choice_map = {
        "minute": ip_time_min(ipaddress),
        "hour": ip_time_hour(ipaddress),
    }

    return module.exit_json(hour=choice_map['hour'], minute=choice_map['minute'])

if __name__ == '__main__':
    main()
