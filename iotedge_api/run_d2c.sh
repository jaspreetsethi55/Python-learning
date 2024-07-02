#Activate virtual env
#source /home/jaspreet/venv3.7/bin/activate
. /home/jaspreet/venv3.7/bin/activate

#Go to respective directory
cd /home/jaspreet/iotedge_api

#run script
#python send_eventhub_message_1500.py
#python send_eventhub_message.py
python send_eventhub_topo.py
#send_eventhub_topo.py

