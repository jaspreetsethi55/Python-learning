source =    {
      "instrument_id":19296285,
      "master_information":{
         "instrument_master":{
            "apex_asset_type":7,
            "apex_asset_type_descr":{'key' : {'c':8, 'd':3, 'e':8} },
            "child_issue_ind":'false',
            "country_of_risk":"ru",
            "eval_quotation_basis":1,
            "instrument_type":4,
            "instrument_type_descr":"equity",
            "primary_currency_code":"usd",
            "primary_exchange":"rusx",
            "primary_market_code":"misx",
            "primary_name":"rub1(usd)",
            "accrued_interest":{
               "ex_div_date_ind":'false'
            }
         },
      }
    }

target =    {
      "instrument_id":19296285,
      "master_information":{
         "instrument_master":{
            "apex_asset_type":7,
            "apex_asset_type_descr":{'key' : {'c':8, 'd':5} },
            "child_issue_ind":'false',
            "country_of_risk":"ru",
            "eval_quotation_basis":1,
            "instrument_type":4,
            "instrument_type_descr":"equity",
            "primary_currency_code":"usd",
            "primary_exchange":"rusx",
            "primary_market_code":"misx",
            "primary_name":"rub1(usd)",
            "accrued_interest":{
               "ex_div_date_ind":'true'
            }
         },
      }
    }



import ast
import argparse

class StructDiff:


    def __init__(self,source,target):
        self.source = source
        self.target = target

    @staticmethod
    def get_paths(struct):
        paths = []
        if isinstance(struct, dict):  # found a dict-like structure...
            for k, v in struct.items():  # iterate over it
                paths.append([k])  # add the current child path
                paths += [[k] + x for x in StructDiff.get_paths(v)]  # get sub-paths, extend with the current

        # else, check if a list-like structure, remove if you don't want list paths included
        elif isinstance(struct, list) and not isinstance(struct, str):
            for i, v in enumerate(struct):
                paths.append([i])
                paths += [[i] + x for x in StructDiff.get_paths(v)]  # get sub-paths, extend with the current
        return paths
    
    @staticmethod
    def get_struct(struct_file):
        with open(struct_file) as f:
            return ast.literal_eval(f.read())

    @classmethod
    def from_file(cls,source_file,target_file):
        return cls(cls.get_struct(source_file),cls.get_struct(target_file))        

    ##Getting value of any path(in form of list) from any structure type
    @staticmethod
    def deref_multi(data, keys):
        return StructDiff.deref_multi(data[keys[0]], keys[1:]) if keys else data

    def compare(self):
        ##getting all desired paths of any given structure
        source_paths,target_paths = self.__class__.get_paths(self.source),self.__class__.get_paths(self.target)

        matched = None
        num = 0

        ##Looping over structure
        while num < len(source_paths):

            ##Indentying missing path
            if source_paths[num] not in target_paths:
                print("MISSING JPATH IN TARGET,{}".format('.'.join(str(v) for v in source_paths[num])))
                num = num + 1
                continue

            ##If parent path matched, then not matching child paths - saving memory/time
            if source_paths[num][0] == matched:
                num=num+1
                continue

            ##If parent path
            if len(source_paths[num]) == 1:
                source,target = self.source[source_paths[num][0]], self.target[source_paths[num][0]]
                if(source == target): ##if values in both structure matches
                    matched = source_paths[num][0]
                
                ##if parent not matches, last parent node(single by dfault) or checking if its single parent  
                elif num == len(source_paths)-1 or source_paths[num][0] != source_paths[num+1][0]:
                #elif isinstance(source,(int,str)) or isinstance(target,(int,str)):
                    print('MISMATCH,{},{},{}'.format('.'.join(source_paths[num]),source,target))
            else:
                current_jpath = '.'.join(str(v) for v in source_paths[num])
                next_jpath = '.'.join(str(v) for v in source_paths[num+1][:-1]) if num < len(source_paths)-1 else None

                if current_jpath != next_jpath:
                    source,target = StructDiff.deref_multi(self.source,source_paths[num]),StructDiff.deref_multi(self.target,source_paths[num])
                    if source != target:
                        print('MISMATCH,{},{},{}'.format(current_jpath,source,target))

            num = num + 1

        for path in target_paths:
            if path not in source_paths:
                print("MISSING JPATH IN SOURCE,{}".format('.'.join(str(v) for v in path)))

script_description = '''
This script carries out difference between 2 data structures(E.g. json).
We can either pass these data stuctures in script or in files as an argument to script
'''

parser = argparse.ArgumentParser(description = script_description)
parser.add_argument("-ff","--from_file",help="Passing data structures in file as an argument to script. Also used options -sf and -tf to pass source_file and target_file data structures",required=False)
parser.add_argument("-sf","--source_file",help="Source file.",required=False)
parser.add_argument("-tf","--target_file",help="Target file.",required=False)

args = parser.parse_args()
from_file = args.from_file
source_file = args.source_file
target_file = args.target_file

if __name__ == '__main__':
   
    if from_file:
            cmp_obj = StructDiff.from_file(source_file,target_file)
        else:
            raise Exception("Please specify source and target files with data structures")

    elif source and target:
        cmp_obj = StructDiff(source,target)
    
    else:
        raise Exception("Please specify source and target variable with data structures")
    #print(cmp_obj)
    cmp_obj.compare()

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
