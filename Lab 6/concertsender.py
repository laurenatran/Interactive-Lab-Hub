import paho.mqtt.client as mqtt
import uuid

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)


channels = ['section', 'bathroom 1','bathroom 2','emergency','food 1', ]
messages = ['hi!',
            'dance!',
            'line is 0-10 people',
            'line is 10-25 people',
            'line is 25-40 people', 
            'line is greater than 40 people', 
            'help needed' ]

channel_state = 0
message_state = 0


while True:
	cmd = channels[channel_state]
	if ' ' in cmd:
		print('sorry white space is a no go for topics')
	else:
		topic = f"IDD/{cmd}"
		print(f"now writing to topic {topic}")
		while True:
			val = messages[message_state]
			if val =='new-topic':
				break
			else:
				client.publish(topic, val)