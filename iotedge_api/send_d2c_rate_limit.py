import requests
from ratelimit import limits, RateLimitException, sleep_and_retry
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from datetime import datetime
import json
from itertools import product


DIAGNOSTIC_MESSAGE = '''{"syslog5424_host":"device_id", "orId":"or_id", "syslog5424_ts":"timestamp","syslog5424_msg_json":{"Interfaces":[{"ColorimetryMeasured":"sRGB","ColorimetryUser":"auto","Connected":false,"Format":"video","LinkStatus":{"BPC":0,"LaneCount":0,"LineRate":"20 (HBR2)","LinkErrors":0,"Trained":false,"TrainingAttempts":0},"Name":"dpIn0","Resolution":"0x0p0","State":"OK","Stereo":false,"Syncs":false,"Type":"encoder"},{"ColorimetryMeasured":"sRGB","ColorimetryUser":"auto","Connected":true,"Format":"video","Name":"generator0","Resolution":"0x0p60000","State":"OK","Stereo":false,"Streams":[],"Syncs":true,"Type":"encoder"},{"Connected":false,"Format":"audio","Input":"line-in","Name":"audioIn","State":"OK","Type":"encoder"},{"Connected":false,"Format":"audio","HasLayout":true,"Name":"audioOut","Output":"line-out","State":"OK","Type":"decoder"},{"Connected":false,"Format":"usb","Name":"USBPeripherals","State":"OK","Type":"decoder"},{"Connected":false,"Format":"usb","Name":"USBHost","State":"OK","Type":"encoder"}],"Logserver":{"Condition":"All messages OK","Messages":{"Dropped":0,"Processed":23447,"Queued":0,"Written":23447},"OperatingRoomId":"or_id","ServerIpAddress":"10.99.113.9","ServerPort":"6514","State":"OK"},"Network":{"Interfaces":[{"IPAddress":"10.99.113.31","MACAddress":"b0:d5:cc:79:50:af","Name":"eth0","RxBytes (MB)":2234,"RxErrors":0,"RxPackets":11804860,"RxRate (kbps)":0,"SFP10GEthType":"10G BASE - SR","SFPConnectorType":"LC","SFPRevision":"G4.1","SFPRxPower (dBm)":-2.3711261870612077,"SFPSerial":"AD16323013Y","SFPTemperature (degr.C)":61,"SFPTxPower (dBm)":-2.6312563835157747,"SFPVendor":"AVAGO","SFPVoltage (V)":3.3250000000000002,"State":"OK","TxBytes (MB)":277,"TxPackets":1151409,"TxRate (kbps)":0,"UptimeAddress (s)":1690743,"UptimeLink (s)":1690743},{"IPAddress":"10.99.113.12","MACAddress":"b2:d5:cc:79:50:af","Name":"eth1","RxBytes (MB)":2282,"RxErrors":0,"RxPackets":10443375,"RxRate (kbps)":0,"SFP10GEthType":"10G BASE - SR","SFPConnectorType":"LC","SFPRevision":"G4.1","SFPRxPower (dBm)":-3.1363189652696382,"SFPSerial":"AD163230139","SFPTemperature (degr.C)":62,"SFPTxPower (dBm)":-2.6672246606741821,"SFPVendor":"AVAGO","SFPVoltage (V)":3.3218000000000001,"State":"OK","TxBytes (MB)":1,"TxPackets":28237,"TxRate (kbps)":0,"UptimeAddress (s)":1690743,"UptimeLink (s)":1690743}]},"RtspServer":{"Format":"streaming","Media":[],"Name":"rtspserver","RtspConnections":[],"RtspSessions":[],"State":"OK","Type":"streaming"},"System":{"BootCount":27,"CPUFanPWM (%)":34,"CPUFanSpeed (RPM)":4230,"CPULoad (%)":100,"CPUTemperature (degr.C)":"cpu_temp","FPGAFanPWM (%)":34,"FPGAFanSpeed (RPM)":3450,"FPGATemperature (degr.C)":68,"FreeRAM (%)":89,"Name":"device_id","ProductPartNumber":"K9303078A","ProductSerialNumber":"2530080634","ProductionDate":"2016-11-15","SoftwareVersion":"2.5.2-12-g324bee9","State":"OK","UpTime (s)":1690751,"name":"System"},"XmppAgents":[{"Name":"xmppagent","Type":"edp","edp server":"","errormessage":"","state":"OK","status":"disabled","xmpp_error":""}]}}'''

TOPOLOGY_MESSAGE = '''{"syslog5424_msg":{"topology":[{"Hostname":"nms_id","cluster":["10.99.112.3"],"interfaces":["eth0"],"version":"1.18.04-5e298","ReleaseVersion":"1.18.04.5e298678e36e1396d4e806ee822f890591f53a5b"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_1","guid":"guid_1","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_2","guid":"guid_2","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_3","guid":"guid_3","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_4","guid":"guid_4","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"},{"interfaces":["audioIn","eth","dpIn0","audioOut"],"Hostname":"device_id_5","guid":"guid_5","Gender":"ENCODER","Firmware":"2.7.1-3-gda67ad2","class":"MNA-240","status":"online","ReleaseVersion":"2.8.0-37-gfae5aa0"}],"orId":"or_id","events":[{"mode-online":"d9b13d40-0870-1c02-e000-b0d5cc786dd31"}],"timestamp":"time_stamp"}}''' 


URL = 'http://10.98.0.167:80/api/v1/devices/messages'

##TS is for test simulator
#OR_ID = ('NOI-IN-TSA-', 'NOI-IN-TSB-', 'NOI-IN-TSC-', 'NOI-IN-TSD-', 'NOI-IN-TSE-')
PARTNER_ID = 'NOI-IN-TSA-'
DEVICE_ID = 'mna-240-enc-1234567-'

####Diagnostic message settings
OR_ID_RANGE = list(range(1,6))
DEVICE_ID_RANGE = list(range(1,21))
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
          #"message": json.loads(message)
          "message": { 'temp' : 45 }
          #"deviceId": "test-d2c"
        }
      ],
      "responseCallback": "https://webhook.site/9cdf068c-2642-467a-aaff-8876c3a4dcf9"
    }

    headers = {'Content-type': 'application/json', 'x-correlation-id': TIMESTAMP , 'Accept': 'application/json'}
    return request_json,headers


def send_d2c_request(message_type):
    message = ''
    if 'diag' in message_type:
        message = get_diagnostic_message()
    elif 'topo' in message_type:
        message = get_topology_message()

    request_json,headers = set_request_params(message)
    r = requests.post(URL, json=request_json, headers=headers)
    return r

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 5
MESSAGE_TYPE = 'diag'


@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def access_rate_limited_api(count):
    resp = send_d2c_request(MESSAGE_TYPE)
    return count,resp
    #print(f"{count}.{resp.text}")    

num_of_messages = 0

if 'diag' in MESSAGE_TYPE:
    num_of_messages = len(or_device_combination)
elif 'topo' in MESSAGE_TYPE:
    num_of_messages = len(topo_device_combination)

with PoolExecutor(max_workers=7) as executor:
    #for _ in executor.map(access_rate_limited_api, range(60)):
    for count,resp in executor.map(access_rate_limited_api, range(num_of_messages)):
        #pass
        print((f"{count}:{resp.text}"))

