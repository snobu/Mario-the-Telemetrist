from azure.servicebus import ServiceBusService
from threading import Thread
from blessings import Terminal

namespace = 'breakingnews'
eventhubname = 'marioevents'
sasname = 'send'
# Read Event Hub key into sasvalue
# (Cheap workaround to not store secrets in GitHub)
with open('data/telemetry/key_eh', 'r') as secret:
    sasvalue = secret.read().replace('\n', '')

sbs = ServiceBusService(namespace,
                        shared_access_key_name=sasname,
                        shared_access_key_value=sasvalue)
t = Terminal()

def fork_and_send(msg):
    print 'Event {t.magenta}{msg}{t.normal} sent to {t.green}{t.bold}Event Hub{t.normal}'.format(t=t, msg=msg)
    json_encoded_msg = '{ "DeviceId": "Mac", "Application": "Mario", "Event": "' + msg + '" }'
    sbs.send_event(eventhubname, json_encoded_msg)

def send_event_async(msg):
    thread = Thread(target = fork_and_send, args = (msg, ))
    thread.start()
