#!/usr/bin/python3.4

class structdiff:

    def __init__(self,source,target):
        self.source = source
        self.target = target

    def get_paths(struct):
        paths = []
        if isinstance(struct, dict):  # found a dict-like structure...
            for k, v in struct.items():  # iterate over it
                paths.append([k])  # add the current child path
                paths += [[k] + x for x in get_paths(v)]  # get sub-paths, extend with the current

        # else, check if a list-like structure, remove if you don't want list paths included
        elif isinstance(struct, list) and not isinstance(struct, str):
            for i, v in enumerate(struct):
                paths.append([i])
                paths += [[i] + x for x in get_paths(v)]  # get sub-paths, extend with the current
        return paths

##Getting value of any path(in form of list) from any structure type
def deref_multi(data, keys):
    return deref_multi(data[keys[0]], keys[1:]) if keys else data

def list_to_jpath(l):
    return 
##getting all desired paths of any given structure
json1_paths,json2_paths = get_paths(json1),get_paths(json2)

matched = None
num = 0

##Looping over structure
while num < len(json1_paths):

    ##Indentying missing path
    if json1_paths[num] not in json2_paths:
        print("Missing jpath in target,{}".format('.'.join(str(v) for v in json1_paths[num])))
        num = num + 1
        continue

    ##If parent path matched, then not matching child paths - saving memory/time
    if json1_paths[num][0] == matched:
        num=num+1
        continue

    ##If parent path
    if len(json1_paths[num]) == 1:
        source,target = json1[json1_paths[num][0]], json2[json1_paths[num][0]]
        if(source == target): ##if values in both structure matches
            matched = json1_paths[num]
        
        ##if parent not matches, last parent node(single by dfault) or checking if its single parent  
        elif num == len(json1_paths)-1 or json1_paths[num][0] != json1_paths[num+1][0]:
        #elif isinstance(source,(int,str)) or isinstance(target,(int,str)):
            print('.'.join(json1_paths[num]),source,target)
    else:
        current_jpath = '.'.join(str(v) for v in json1_paths[num])
        next_jpath = '.'.join(str(v) for v in json1_paths[num+1][:-1]) if num < len(json1_paths)-1 else None

        if current_jpath != next_jpath:
            source,target = deref_multi(json1,json1_paths[num]),deref_multi(json2,json1_paths[num])
            if source != target:
                print(current_jpath,source,target)

    num = num + 1                


'''
['global_information']
['global_information', 'organization_information']
['global_information', 'organization_information', 'classifications']
['global_information', 'organization_information', 'classifications', 'primary_naics_code']
['global_information', 'organization_information', 'classifications', 'sic_code']
['global_information', 'country_information']
['global_information', 'country_information', 'instrument_country_information']
['global_information', 'country_information', 'instrument_country_information', 'country_code']
['global_information', 'country_information', 'instrument_country_information', 'holiday_schedule']
['master_information']
['master_information', 'instrument_master']
['master_information', 'instrument_master', 'apex_asset_type_descr']
['master_information', 'instrument_master', 'federal_tax_status_descr']
['master_information', 'instrument_master', 'primary_exchange']
['master_information', 'instrument_master', 'primary_currency_code']
['master_information', 'instrument_master', 'accrued_interest']
['master_information', 'instrument_master', 'accrued_interest', 'ex_div_date_ind']
['master_information', 'instrument_master', 'instrument_type_descr']
['instrument_id']
'''
