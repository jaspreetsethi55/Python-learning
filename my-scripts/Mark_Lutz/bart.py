import requests
import json

#url ='http://api.bart.gov/api/etd.aspx?cmd=etd&orig=ALL&key=MW9S-E7SL-26DU-VV8V&json=y'
url ='http://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V&json=y'
with requests.get(url,verify=False) as response:
    #response_text = response.text.rstrip()

    print(response.text)
