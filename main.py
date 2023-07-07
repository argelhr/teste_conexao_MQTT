# Fonte,  https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
# python 3.6

import random
import time
import paramiko

from paho.mqtt import client as mqtt_client

broker = 'ubuntu@tsi1.duckdns.org'
port = 1883
topic = "sensor1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# username = 'emqx'
# password = 'public'

# Configuração SSH
#ssh_host = 'ubuntu@tsi1.duckdns.org'
#ssh_port = 22
#ssh_username = 'argel'
#ssh_private_key_path = ""

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"counter: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    #Conexão SSH
    #ssh = paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.connect(ssh_host, ssh_port, ssh_username, key_filename=ssh_private_key_path)

    # Conexão MQTT
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
