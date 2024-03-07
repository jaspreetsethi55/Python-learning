#!/usr/bin/python3.4

###############
##Created on: 2020-01-07
##Author: Jaspreet Sethi
##Task: The script carries queries web-service and gives data for fields set up in script in form of csv file.
##Usage: python3.4 get_ws_data.py [-h] -f FILENAME
################

import requests
from jsonpath_rw import jsonpath, parse
from decimal import Decimal
import sys
import json
import re
import argparse
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

script_description = '''
This script carries queries web-service and gives data for fields set up in script in form of csv file.
'''

parser = argparse.ArgumentParser(description = script_description)
parser.add_argument("-f","--filename",help="Input file containing entity_type and entity, seperated by comma. E.g. eid,1234567", required=True)

args = parser.parse_args()

fields_to_get = ['instrument_id',
    'master_information.instrument_master.instrument_status',
    'master_information.instrument_master.instrument_status_descr']

#getting jpath result
def get_jpath_result(json_data,jpath):
    path = parse('$.' + jpath)

    res = ''
    for match in path.find(json_data):
        res = match.value
        ##For now, getting only single value from jpath
        break

    return res

#Get url content
def get_url_data(entity_type,entity):
    url = 'https://apex.pt.interactivedata.com/apex/ws/v1?entities=' + entity_type + ':' + entity + '&indent=true'
    with requests.get(url, auth=('d4clsint', 'abc12345'),verify=False) as response:
        return json.loads(response.text,parse_float=Decimal)[0] ##Intacting floating point decimals
        #return response.json()[0]



input_file = args.filename
for line in open(input_file):
    entity_type,entity = line.rstrip().split(',') ##Removing new-line and splitting

    data = get_url_data(entity_type,entity)
    print(','.join([ str(get_jpath_result(data,jpath)) for jpath in fields_to_get ]))

