#########################
##Created on: 2023-08-24
##Author: Jaspreet Sethi
##Task: This script simulates the NexxisCare message streaming via sending the diag/topo message to EventHub via Iot Edge.
##Usage:  python send_d2c_rate_limit_diag-topo.py [-h] -mt MESSAGE_TYPE [-d DURATION] [-mc MAX_CALLS] [-ac ASYNC_CALLS]
##optional arguments:
##  -h, --help            show this help message and exit
##  -mt MESSAGE_TYPE, --message_type MESSAGE_TYPE
##                        Type of message to simulate i.e. diagnostic or
##                        topology. Possible values:diag or topo
##  -d DURATION, --duration DURATION
##                        Message duration/period i.e. time period in seconds
##                        for which we need to send messages
##  -mc MAX_CALLS, --max_calls MAX_CALLS
##                        Maximum calls that can be send in duration
##  -ac ASYNC_CALLS, --async_calls ASYNC_CALLS
##                        Number of async/parallel calls for sending the
##                       messages following duration & max_calls criteria
##
##########################


import requests
from ratelimit import limits, RateLimitException, sleep_and_retry
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from datetime import datetime
import json
from itertools import product
import argparse
import socket
import os

DIAGNOSTIC_MESSAGE = '''{"syslog5424_host":"device_id","orId":"or_id","syslog5424_ts":"timestamp","syslog5424_msg_json":{"Interfaces":[{"ColorimetryMeasured":"sRGB","ColorimetryUser":"auto","Connected":false,"Format":"video","GenlockMode":"","Genlocked":"","GenlockSource":"","LinkStatus":{"BPC":0,"LaneCount":0,"LineRate":"20(HBR2)","LinkErrors":0,"Trained":false,"TrainingAttempts":0},"Name":"dpIn0","Resolution":"0x0p0","State":"OK","Stereo":false,"Syncs":false,"Type":"encoder"},{"ColorimetryMeasured":"sRGB","ColorimetryUser":"auto","Connected":true,"Format":"video","Name":"generator0","GenlockMode":"","Genlocked":"","GenlockSource":"","Resolution":"0x0p60000","State":"OK","Stereo":false,"Streams":[],"Syncs":true,"Type":"encoder"},{"Connected":false,"GenlockMode":"","Genlocked":"","GenlockSource":"","Format":"audio","Input":"line-in","Name":"audioIn","State":"OK","Type":"encoder"},{"Connected":false,"GenlockMode":"","Genlocked":"","GenlockSource":"","Format":"audio","HasLayout":true,"Name":"audioOut","Output":"line-out","State":"OK","Type":"decoder"},{"Connected":false,"GenlockMode":"","Genlocked":"","GenlockSource":"","Format":"usb","Name":"USBPeripherals","State":"OK","Type":"decoder"},{"Connected":false,"GenlockMode":"","Genlocked":"","GenlockSource":"","Format":"usb","Name":"USBHost","State":"OK","Type":"encoder"}],"Logserver":{"Condition":"AllmessagesOK","Messages":{"Dropped":0,"Processed":23447,"Queued":0,"Written":23447},"OperatingRoomId":"or_id","ServerIpAddress":"10.99.113.9","ServerPort":"6514","State":"OK"},"Network":{"Interfaces":[{"IPAddress":"10.99.113.31","MACAddress":"b0: d5: cc: 79: 50: af","Name":"eth0","RxBytes(MB)":2234,"RxErrors":0,"RxPackets":11804860,"RxRate(kbps)":0,"SFP10GEthType":"10GBASE-SR","SFPConnectorType":"LC","SFPRevision":"G4.1","SFPRxPower(dBm)":-2.3711261870612079,"SFPSerial":"AD16323013Y","SFPTemperature(degr.C)":61,"SFPTxPower(dBm)":-2.6312563835157749,"SFPVendor":"AVAGO","SFPVoltage(V)":3.325,"State":"OK","TxBytes(MB)":277,"TxPackets":1151409,"TxRate(kbps)":0,"UptimeAddress(s)":1690743,"UptimeLink(s)":1690743},{"IPAddress":"10.99.113.12","MACAddress":"b2: d5: cc: 79: 50: af","Name":"eth1","RxBytes(MB)":2282,"RxErrors":0,"RxPackets":10443375,"RxRate(kbps)":0,"SFP10GEthType":"10GBASE-SR","SFPConnectorType":"LC","SFPRevision":"G4.1","SFPRxPower(dBm)":-3.136318965269638,"SFPSerial":"AD163230139","SFPTemperature(degr.C)":62,"SFPTxPower(dBm)":-2.667224660674182,"SFPVendor":"AVAGO","SFPVoltage(V)":3.3218,"State":"OK","TxBytes(MB)":1,"TxPackets":28237,"TxRate(kbps)":0,"UptimeAddress(s)":1690743,"UptimeLink(s)":1690743}]},"RtspServer":{"Format":"streaming","Media":[],"Name":"rtspserver","RtspConnections":[],"RtspSessions":[],"State":"OK","Type":"streaming"},"System":{"BootCount":27,"CPUFanPWM(%)":34,"CPUFanSpeed(RPM)":4230,"CPULoad(%)":100,"CPUTemperature(degr.C)":90,"FPGAFanPWM(%)":34,"FPGAFanSpeed(RPM)":3450,"FPGATemperature(degr.C)":68,"FreeRAM(%)":89,"Name":"device_id","ProductPartNumber":"K9303078A","ProductSerialNumber":"2530080634","ProductionDate":"2016-11-15","SoftwareVersion":"2.5.2-12-g324bee9","State":"OK","UpTime(s)":1690751,"name":"System"},"XmppAgents":[{"Name":"xmppagent","Type":"edp","edpserver":"","errormessage":"","state":"OK","status":"disabled","xmpp_error":""}]}}'''

TOPOLOGY_MESSAGE = '''{"syslog5424_msg":{"topology":[{"Hostname":"nms_id","cluster":["10.99.112.3"],"interfaces":["eth0"],"version":"1.18.04-5e298","ReleaseVersion":"1.18.04.5e298678e36e1396d4e806ee822f890591f53a5b"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_1","guid":"d9b13d40-0870-1c02-e000-b0d5cc786dd31","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_2","guid":"d9b13d40-0870-1c02-e000-b0d5cc786dd32","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_3","guid":"d9b13d40-0870-1c02-e000-b0d5cc786dd33","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_4","guid":"d9b13d40-0870-1c02-e000-b0d5cc786dd34","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_5","guid":"d9b13d40-0870-1c02-e000-b0d5cc786dd35","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"}],"orId":"or_id","events":[{"mode-online":"d9b13d40-0870-1c02-e000-b0d5cc786dd31"}],"timestamp":"time_stamp"}}
'''


##TS is for test simulator
#OR_ID = ('NOI-IN-TSA-', 'NOI-IN-TSB-', 'NOI-IN-TSC-', 'NOI-IN-TSD-', 'NOI-IN-TSE-')
PARTNER_ID = 'NOI-IN-TSA-'
DEVICE_ID = 'mna-240-enc-1234567-'

####Diagnostic message settings
OR_ID_RANGE = list(range(1,500))
DEVICE_ID_RANGE = list(range(1,20))
or_device_combination = [list(tup) for tup in product(OR_ID_RANGE, DEVICE_ID_RANGE)]


####Topology message settings
TOPOLOGY_MESSAGE_ITERATION = list(range(1,10))
GUID = "d9b13d40-0870-1c02-e000-b0d5cc786dd"
NMS_ID = "nms-20773246630300"
topo_device_combination = [list(tup) for tup in product(OR_ID_RANGE, TOPOLOGY_MESSAGE_ITERATION)]

TIMESTAMP = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
TEMPERATURE = '90'


def get_topology_message():
    or_id = PARTNER_ID + str(or_device_combination[0][0])
    nms_id = NMS_ID + str(or_device_combination[0][0])
    message = TOPOLOGY_MESSAGE.replace("time_stamp", TIMESTAMP).replace("or_id", or_id).replace("nms_id", nms_id)

    ##For now, above topo message is having 1 nms dict, 5 device/guid dict, so setting below the same
    for i in range(1,6):
        device_id = "device_id_" + str(i)
        guid_id = "guid_" + str(i)

        device_id_value = DEVICE_ID + str(or_device_combination[0][0]) + str(i)
        guid_value = GUID + str(or_device_combination[0][0]) + str(i)

        message = message.replace(device_id, device_id_value).replace(guid_id, guid_value)

    del or_device_combination[0]

    return message 

def get_diagnostic_message():
    or_id, device_id = PARTNER_ID + str(or_device_combination[0][0]) , DEVICE_ID + str(or_device_combination[0][0]) + str(or_device_combination[0][1])
    del or_device_combination[0]

    message = DIAGNOSTIC_MESSAGE.replace("timestamp", TIMESTAMP).replace("device_id", device_id).replace("or_id", or_id).replace("cpu_temp", TEMPERATURE)
    return message 


def set_request_params(message):
   
    request_json = {
      "data": [
        {
          "message": json.loads(message)
          #"message": { 'a' : 1 }
          #"deviceId": "test-d2c"
        }
      ],
      "responseCallback": "https://webhook.site/9cdf068c-2642-467a-aaff-8876c3a4dcf9"
    }

    headers = {'Content-type': 'application/json', 'x-correlation-id': TIMESTAMP , 'Accept': 'application/json'}
    return request_json,headers


def send_d2c_request(message_type,url):
    message = ''
    if 'diag' in message_type:
        message = get_diagnostic_message()
    elif 'topo' in message_type:
        message = get_topology_message()

    json_message = json.loads(message)
    kafka_cli = f'./kafka-console-producer.sh --broker-list b-1.nexxismsktst03.uhbz4s.c9.kafka.eu-west-1.amazonaws.com:9092  --topic test_diag < {json_message}'
    r = os.system(kafka_cli)
    return r


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # connect() for UDP doesn't send packets
    s.connect(('10.0.0.0', 0))
    
    return s.getsockname()[0]


script_description = '''
This script simulates the NexxisCare message streaming via sending the diag/topo message to EventHub via Iot Edge.
'''

parser = argparse.ArgumentParser(description = script_description)
parser.add_argument("-mt","--message_type",help="Type of message to simulate i.e. diagnostic or topology. Possible values:diag or topo", required=True)
parser.add_argument("-d","--duration",help="Message duration/period i.e. time period in seconds for which we need to send messages",required=False,default=60)
parser.add_argument("-mc","--max_calls",help="Maximum calls that can be send in duration",required=False,default=5)
parser.add_argument("-ac","--async_calls",help="Number of async/parallel calls for sending the messages following duration & max_calls criteria",required=False,default=3)
parser.add_argument("-ip","--ip_address",help="This should be IP address of machine where IOT Edge is installed. Default is machine IP",required=False,default=get_ip())

args = parser.parse_args()

##Possible values 'diag'  or 'topo'
MESSAGE_TYPE = args.message_type

DURATION_IN_SEC = int(args.duration)
MAX_CALLS_IN_DURATION = int(args.max_calls)
ASYNC_CALLS = args.async_calls
IP_ADDRESS = args.ip_address

KAFKA_URL = f'b-1.nexxismsktst03.uhbz4s.c9.kafka.eu-west-1.amazonaws.com:9092'

@sleep_and_retry
#@limits(calls=MAX_CALLS_IN_DURATION, period=DURATION_IN_SEC)
@limits(calls=1000, period=15)
def access_rate_limited_api(count):
    resp = send_d2c_request(MESSAGE_TYPE, KAFKA_URL)
    return count,resp
    #print(f"{count}.{resp.text}")    

num_of_messages = 0

if 'diag' in MESSAGE_TYPE:
    num_of_messages = len(or_device_combination)
elif 'topo' in MESSAGE_TYPE:
    num_of_messages = len(topo_device_combination)

with PoolExecutor(max_workers=ASYNC_CALLS) as executor:
    for count,resp in executor.map(access_rate_limited_api, range(num_of_messages)):
        print((f"{count}:{resp.text}"))

