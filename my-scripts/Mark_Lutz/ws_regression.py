#!/usr/bin/python3.4

###############
##Created on: 2019-12-30
##Author: Jaspreet Sethi
##Task: The script hits the PPE and PROD web-service based on inputs given in config file and compares the data between them and shows it in 3 different output formats. We can run any(gsm/gpm/cep/etc) web-service regression via this script.
##Usage: usage: ws_regression.py [-h] -f FILENAME -c CONFIG [-d DIRECTORY]
################

import requests
import sys
import json
import re
import argparse
import os
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

script_description = '''
This script carries out web-service regresssion(based on inputs given in config file ws_regression.config) by comparing output(in json) returned from two different environments(PPE and PROD). We can run any(gsm/gpm/cep/etc) web-service regression via this script as per inputs given.
'''

parser = argparse.ArgumentParser(description = script_description)
parser.add_argument("-c","--config",help="Config file containing regression_type,ppe_url,prod_url,ppe_params,prod_params", required=True)
parser.add_argument("-rt","--regression_type",help="Regression_type for which we want to run the script, we can pass single or multiple seperated by comma.", required=True)
parser.add_argument("-d","--directory",help="Output directory. If not specified directory named 'output' will be created(if not there)",required=False,default='output')

args = parser.parse_args()

##Reading config parameters and storing as a structural dict
def read_config(config_file):
    config = open(config_file)

    #Reading header via ignoring first column
    header = next(config).rstrip().split('|')[1:]

    ##Getting environment(from header) to run regression between 
    env1,env2 = re.findall(r'\((\w+)\)',str(header))

    ##Removing env from header
    header = [ re.sub('\(\w+\)','',name)  for name in header ]

    config_dict = {}
    for line in config:
        regression_type,*values = line.rstrip().split('|')
        config_dict[regression_type] = dict(zip(header,values))

    return config_dict,env1,env2


#Get url content
def get_url_data(url):
    #with requests.get(url, auth=('d4clsint', 'abc12345'),verify=False) as response:
    with requests.get(url, auth=('d4apexw2','Apex2017'),verify=False) as response:
        response_text = response.text.rstrip()

        #re.subn() perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made)
        (response_text_replaced,num_of_sub) = re.subn('"valoren_code":(\d+)','"valoren_code":"\\1"',response_text)

        if(num_of_sub):
            print("Added double quotes to valoren_code")

        return response_text_replaced


#recursively sorting json - key point is to make both jsons in same order
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


##Printing formatted diff results
def print_formatted_diff(my_id,env1_res,env2_res):
    env1_res_list, env2_res_list = env1_res.split('\n'), env2_res.split('\n')

    env1_res_len,env2_res_len = len(env1_res_list),len(env2_res_list)
    min_len = env1_res_len if(env1_res_len < env2_res_len) else env2_res_len

    error_file = output_dir + '/' + my_id + '_diff.txt'
    with open(error_file,'w') as f:
        f.write("{} TEST FAILED {}\n\n".format('-' * 68, '-' * 86))
        f.write("{} PPE-{} {}".format('-' * 28,my_id,'-' * 28))
        f.write("{} PROD-{} {}\n".format('-' * 28,my_id,'-' * 52))

        for index in range(min_len):
            f.write('{}:{: <70}| {}\n\n'.format(index, env1_res_list[index], env2_res_list[index]))


##Load the reponse in file
def load_in_file(my_id,env,response):
    file_name = out_diff_dir + '/' + my_id + '_' + env + '.txt'

    fh = open(file_name,'w')
    fh.write(response)
    fh.close()

    return file_name

##Reading arguments
config_file = args.config
regression_type = args.regression_type.split(',')

config_dict,env1,env2 = read_config(config_file)
print("Config_dict:\n{}\nEnv:{} vs {}".format(config_dict,env1,env2))

##Looping over regression types for which script needs to run
for reg_type in regression_type:

    if reg_type not in config_dict:
        print("Unknown regression type given:{}".format(reg_type))
        continue
 
    output_dir = args.directory + '_' + reg_type + '_' + datetime.today().strftime('%Y_%m_%d')

    ##Creating output directory and adding hhmmss to name if output dir of output_cep_yy_mm_dd already exists
    if os.path.exists(output_dir):
        output_dir = output_dir + '_' + datetime.today().strftime('%H_%M_%S')
        os.makedirs(output_dir)
    
    all_diff_file = output_dir + '/all_inst_diff.txt'
    out_diff_dir = output_dir + '/diff_inst'

    os.makedirs(out_diff_dir)
    log_file = output_dir + '.log'

    ##Re-directing every print statement to log file
    sys.stdout = open(log_file,'w')
    
    print("Config_dict:\n{}\nEnv:{} vs {}".format(config_dict,env1,env2))
    print("\n########Running {} Regression############\n\n".format(reg_type))

    with open(config_dict[reg_type]['input_file']) as f:

        ##Getting headers of input file, as in input file and config file
        input_file_header,input_file_config_header = next(f).rstrip().split(','),config_dict[reg_type]['input_file_columns'].split(':')
        
        if input_file_header != input_file_config_header:
            print("Headers in input file:{} and config file:{} are different.\nInput file header:{}\nInput file header as per Config file:{}\n".format(config_dict[reg_type]['input_file'],config_file,input_file_header,input_file_config_header))
            continue    

        entity_index = input_file_header.index('entity')

        for line in f:
            entity = line.rstrip().split(',')[entity_index]

            ##Getting input file params ready for url
            entity_params = '&'.join([x + '=' + y for x,y in zip(input_file_header,line.rstrip().split(','))])

            ##converting entity_type=eid&entity=123 to eid:123 
            entity_params = re.sub('entity_type=(\w+)&entity=(\w+)','\\1:\\2',entity_params)

            env1_url = config_dict[reg_type]['env1_url'] + entity_params + '&' + config_dict[reg_type]['env1_params']
            env2_url = config_dict[reg_type]['env2_url'] + entity_params + '&' + config_dict[reg_type]['env2_params']
        
            print(env1_url)
            print(env2_url)
            env1_response = get_url_data(env1_url) #getting env1 url data
            env2_response = get_url_data(env2_url) #getting env2 url data

            env1_response_json = json.loads(env1_response)
            env2_response_json = json.loads(env2_response)

            ord_env1_json,ord_env2_json = ordered(env1_response_json), ordered(env2_response_json)

            if( 'error' in env1_response_json or 'error' in env2_response_json):
                env1_error = env1_response_json.get('error','No env1 error') if(isinstance(env1_response_json, dict)) else 'No env1 error'
                env2_error = env2_response_json.get('error','No env2 error') if(isinstance(env2_response_json, dict)) else 'No env2 error'

                print("Entity:{} failed:\nenv1::{}\nenv2::{}".format(entity,env1_error,env2_error))

            elif(ord_env1_json == ord_env2_json):
                print("{} - Matched".format(entity))
                load_in_file(entity,'MATCHED_ENV1_' + env1.upper(),env1_response)
                load_in_file(entity,'MATCHED_ENV2_' + env2.upper(),env2_response)

            else:
                print("{} - Not Matched".format(entity))

                ##Checking if instruments in both env matches but not for cep(since it doesn't return instruments)
                if(reg_type.lower() != 'cep' and env1_response_json[0]['instrument_id'] != env2_response_json[0]['instrument_id']):
                        print("ENV1{} and ENV2{} instrument does not match".format(env1_response_json[0]['instrument_id'],  env2_response_json[0]['instrument_id']))
              
                print_formatted_diff(entity,env1_response,env2_response)

                ##Writing all differences to a single file
                cmd_1 = """perl -e 'print "{}" . "-" x 68 . "Inst:{}"  . "-" x 82 . "{}"' >> {}""".format('\n\n', entity, '\n' ,all_diff_file)
                os.system(cmd_1)

                cmd_2 = "diff {} {} >> {}".format(load_in_file(entity,'PPE',env1_response),load_in_file(entity,'PROD',env2_response),all_diff_file)
                os.system(cmd_2)
                

