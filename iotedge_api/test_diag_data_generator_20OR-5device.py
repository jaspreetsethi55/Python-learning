from pysyslog import MySSL_TCPClient
import time
from datetime import datetime

iterations = 1
for iteration in range(iterations):
	now = datetime.utcnow()
	timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
	print('Iteration - {}'.format(iteration))
	for or_num in range(3, 5):
		partner_id = "NOI-IN-AAA-"
		or_id = partner_id + str(or_num)
		print(or_id)
		for device in range(1, 21):
			device_id = "mna-240-enc-1234567-" + str(or_num) + str(device)
			print(device_id)
			temperature = '90'
			diagnostic_cpu_temp='<13>1 timestamp device_id diagnostic - - [nexxis@12827 orId="or_id" TIME="timestamp" IP="10.99.114.2"] {"Interfaces":[{"ColorimetryMeasured":"sRGB","ColorimetryUser":"auto","Connected":false,"Format":"video","LinkStatus":{"BPC":0,"LaneCount":0,"LineRate":"20 (HBR2)","LinkErrors":0,"Trained":false,"TrainingAttempts":0},"Name":"dpIn0","Resolution":"0x0p0","State":"OK","Stereo":false,"Syncs":false,"Type":"encoder"},{"ColorimetryMeasured":"sRGB","ColorimetryUser":"auto","Connected":true,"Format":"video","Name":"generator0","Resolution":"0x0p60000","State":"OK","Stereo":false,"Streams":[],"Syncs":true,"Type":"encoder"},{"Connected":false,"Format":"audio","Input":"line-in","Name":"audioIn","State":"OK","Type":"encoder"},{"Connected":false,"Format":"audio","HasLayout":true,"Name":"audioOut","Output":"line-out","State":"OK","Type":"decoder"},{"Connected":false,"Format":"usb","Name":"USBPeripherals","State":"OK","Type":"decoder"},{"Connected":false,"Format":"usb","Name":"USBHost","State":"OK","Type":"encoder"}],"Logserver":{"Condition":"All messages OK","Messages":{"Dropped":0,"Processed":23447,"Queued":0,"Written":23447},"OperatingRoomId":"or_id","ServerIpAddress":"10.99.113.9","ServerPort":"6514","State":"OK"},"Network":{"Interfaces":[{"IPAddress":"10.99.113.31","MACAddress":"b0:d5:cc:79:50:af","Name":"eth0","RxBytes (MB)":2234,"RxErrors":0,"RxPackets":11804860,"RxRate (kbps)":0,"SFP10GEthType":"10G BASE - SR","SFPConnectorType":"LC","SFPRevision":"G4.1","SFPRxPower (dBm)":-2.3711261870612077,"SFPSerial":"AD16323013Y","SFPTemperature (degr.C)":61,"SFPTxPower (dBm)":-2.6312563835157747,"SFPVendor":"AVAGO","SFPVoltage (V)":3.3250000000000002,"State":"OK","TxBytes (MB)":277,"TxPackets":1151409,"TxRate (kbps)":0,"UptimeAddress (s)":1690743,"UptimeLink (s)":1690743},{"IPAddress":"10.99.113.12","MACAddress":"b2:d5:cc:79:50:af","Name":"eth1","RxBytes (MB)":2282,"RxErrors":0,"RxPackets":10443375,"RxRate (kbps)":0,"SFP10GEthType":"10G BASE - SR","SFPConnectorType":"LC","SFPRevision":"G4.1","SFPRxPower (dBm)":-3.1363189652696382,"SFPSerial":"AD163230139","SFPTemperature (degr.C)":62,"SFPTxPower (dBm)":-2.6672246606741821,"SFPVendor":"AVAGO","SFPVoltage (V)":3.3218000000000001,"State":"OK","TxBytes (MB)":1,"TxPackets":28237,"TxRate (kbps)":0,"UptimeAddress (s)":1690743,"UptimeLink (s)":1690743}]},"RtspServer":{"Format":"streaming","Media":[],"Name":"rtspserver","RtspConnections":[],"RtspSessions":[],"State":"OK","Type":"streaming"},"System":{"BootCount":27,"CPUFanPWM (%)":34,"CPUFanSpeed (RPM)":4230,"CPULoad (%)":100,"CPUTemperature (degr.C)":cpu_temp,"FPGAFanPWM (%)":34,"FPGAFanSpeed (RPM)":3450,"FPGATemperature (degr.C)":68,"FreeRAM (%)":89,"Name":"device_id","ProductPartNumber":"K9303078A","ProductSerialNumber":"2530080634","ProductionDate":"2016-11-15","SoftwareVersion":"2.5.2-12-g324bee9","State":"OK","UpTime (s)":1690751,"name":"System"},"XmppAgents":[{"Name":"xmppagent","Type":"edp","edp server":"","errormessage":"","state":"OK","status":"disabled","xmpp_error":""}]}'
			data_part_mod = diagnostic_cpu_temp.replace("timestamp", timestamp).replace("device_id", device_id).replace("or_id", or_id).replace("cpu_temp", temperature)
			data = str(len(data_part_mod)) + ' ' + data_part_mod
			client = MySSL_TCPClient("10.99.112.29", 6514)
			print("TimeStamp when data sent for deiceId {} : {}".format(device_id, timestamp))
			client.send(data)
			print('Data Sent to NIS for device: {}'.format(device_id))
			print(data)
			exit()
	print('wait 60 sec')
	print('Iteration - {}'.format(iteration))
	time.sleep(1)
	
