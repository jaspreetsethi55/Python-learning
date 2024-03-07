import re

class Apex:
    def __init__(self,filename,dbname,sigma):
        self.filename = filename
        self.db = dbname
        self.sigma = sigma

    def get_insts(self):
        yield (line.split('"')[1] for line in self.filename if re.search(r'instrument id='))

client1 = Apex('gsm_init_etd_APEXODS_GSMF0FQE.70.1.20200129T0800-05.xml','Omega.etd','O-Derivative')

for inst in iter(client1.get_insts()):
    print(inst)
