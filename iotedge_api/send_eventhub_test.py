import os
from azure.eventhub import EventHubProducerClient, EventData
import json

CONNECTION_STR = "Endpoint=sb://nexxissandboxtest.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Ekd8fXNpN5BUguwmYhzP8r2e/M0vFAJPm+AEhAnzWhM="
EVENTHUB_NAME = "nexxis_sandbox_eventhub"

#CONNECTION_STR = "Endpoint=sb://iothub-ns-ne-nexxis-25158162-b0438eb667.servicebus.windows.net/;SharedAccessKeyName=service;SharedAccessKey=CwiyhizJG7P/B5mmuwX6t4QKj0szRdJ0sLvmvozjV90="
#EVENTHUB_NAME = "ne-nexxis-sandbox-care-io"

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STR,
    eventhub_name=EVENTHUB_NAME
)
message = json.dumps({'syslog5424_host': 'mna-240-enc-1234567-14', 'orId': 'NOI-IN-TSA-1', 'syslog5424_ts': '2023-09-11T16:27:57.860', 'syslog5424_msg_json': {'Interfaces': [{'ColorimetryMeasured': 'sRGB', 'ColorimetryUser': 'auto', 'Connected': False, 'Format': 'video', 'GenlockMode': '', 'Genlocked': '', 'GenlockSource': '', 'LinkStatus': {'BPC': 0, 'LaneCount': 0, 'LineRate': '20(HBR2)', 'LinkErrors': 0, 'Trained': False, 'TrainingAttempts': 0}, 'Name': 'dpIn0', 'Resolution': '0x0p0', 'State': 'OK', 'Stereo': False, 'Syncs': False, 'Type': 'encoder'}, {'ColorimetryMeasured': 'sRGB', 'ColorimetryUser': 'auto', 'Connected': True, 'Format': 'video', 'Name': 'generator0', 'GenlockMode': '', 'Genlocked': '', 'GenlockSource': '', 'Resolution': '0x0p60000', 'State': 'OK', 'Stereo': False, 'Streams': [], 'Syncs': True, 'Type': 'encoder'}, {'Connected': False, 'GenlockMode': '', 'Genlocked': '', 'GenlockSource': '', 'Format': 'audio', 'Input': 'line-in', 'Name': 'audioIn', 'State': 'OK', 'Type': 'encoder'}, {'Connected': False, 'GenlockMode': '', 'Genlocked': '', 'GenlockSource': '', 'Format': 'audio', 'HasLayout': True, 'Name': 'audioOut', 'Output': 'line-out', 'State': 'OK', 'Type': 'decoder'}, {'Connected': False, 'GenlockMode': '', 'Genlocked': '', 'GenlockSource': '', 'Format': 'usb', 'Name': 'USBPeripherals', 'State': 'OK', 'Type': 'decoder'}, {'Connected': False, 'GenlockMode': '', 'Genlocked': '', 'GenlockSource': '', 'Format': 'usb', 'Name': 'USBHost', 'State': 'OK', 'Type': 'encoder'}], 'Logserver': {'Condition': 'AllmessagesOK', 'Messages': {'Dropped': 0, 'Processed': 23447, 'Queued': 0, 'Written': 23447}, 'OperatingRoomId': 'NOI-IN-TSA-1', 'ServerIpAddress': '10.99.113.9', 'ServerPort': '6514', 'State': 'OK'}, 'Network': {'Interfaces': [{'IPAddress': '10.99.113.31', 'MACAddress': 'b0: d5: cc: 79: 50: af', 'Name': 'eth0', 'RxBytes(MB)': 2234, 'RxErrors': 0, 'RxPackets': 11804860, 'RxRate(kbps)': 0, 'SFP10GEthType': '10GBASE-SR', 'SFPConnectorType': 'LC', 'SFPRevision': 'G4.1', 'SFPRxPower(dBm)': -2.3711261870612077, 'SFPSerial': 'AD16323013Y', 'SFPTemperature(degr.C)': 61, 'SFPTxPower(dBm)': -2.6312563835157747, 'SFPVendor': 'AVAGO', 'SFPVoltage(V)': 3.325, 'State': 'OK', 'TxBytes(MB)': 277, 'TxPackets': 1151409, 'TxRate(kbps)': 0, 'UptimeAddress(s)': 1690743, 'UptimeLink(s)': 1690743}, {'IPAddress': '10.99.113.12', 'MACAddress': 'b2: d5: cc: 79: 50: af', 'Name': 'eth1', 'RxBytes(MB)': 2282, 'RxErrors': 0, 'RxPackets': 10443375, 'RxRate(kbps)': 0, 'SFP10GEthType': '10GBASE-SR', 'SFPConnectorType': 'LC', 'SFPRevision': 'G4.1', 'SFPRxPower(dBm)': -3.136318965269638, 'SFPSerial': 'AD163230139', 'SFPTemperature(degr.C)': 62, 'SFPTxPower(dBm)': -2.667224660674182, 'SFPVendor': 'AVAGO', 'SFPVoltage(V)': 3.3218, 'State': 'OK', 'TxBytes(MB)': 1, 'TxPackets': 28237, 'TxRate(kbps)': 0, 'UptimeAddress(s)': 1690743, 'UptimeLink(s)': 1690743}]}, 'RtspServer': {'Format': 'streaming', 'Media': [], 'Name': 'rtspserver', 'RtspConnections': [], 'RtspSessions': [], 'State': 'OK', 'Type': 'streaming'}, 'System': {'BootCount': 27, 'CPUFanPWM(%)': 34, 'CPUFanSpeed(RPM)': 4230, 'CPULoad(%)': 100, 'CPUTemperature(degr.C)': 90, 'FPGAFanPWM(%)': 34, 'FPGAFanSpeed(RPM)': 3450, 'FPGATemperature(degr.C)': 68, 'FreeRAM(%)': 89, 'Name': 'mna-240-enc-1234567-14', 'ProductPartNumber': 'K9303078A', 'ProductSerialNumber': '2530080634', 'ProductionDate': '2016-11-15', 'SoftwareVersion': '2.5.2-12-g324bee9', 'State': 'OK', 'UpTime(s)': 1690751, 'name': 'System'}, 'XmppAgents': [{'Name': 'xmppagent', 'Type': 'edp', 'edpserver': '', 'errormessage': '', 'state': 'OK', 'status': 'disabled', 'xmpp_error': ''}]}})

#event_data_batch = producer.create_batch()

ors = 25
devices = 40
for i in range(ors):
    event_data_batch = producer.create_batch()
    for j in range(devices):
        event_data_batch.add(EventData(message))
    producer.send_batch(event_data_batch)
print("sent 1000 records")
