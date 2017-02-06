# Init Application Insight clients
from applicationinsights import TelemetryClient
import datetime
from threading import Thread
from blessings import Terminal

# Read Application Insights instrumentation key into instrum_key
# (Cheap workaround to not store secrets in GitHub)
with open('data/telemetry/key_ai', 'r') as secret:
    instrum_key = secret.read().replace('\n', '')

tc = TelemetryClient(instrum_key)
t = Terminal()

def fork_and_send(msg):
    tc.track_event(msg)
    tc.flush()
    print 'Event {t.magenta}{msg}{t.normal} sent to {t.yellow}{t.bold}App Insights{t.normal}'.format(t=t, msg=msg)
    return True

def send_event_async(msg):
    thread = Thread(target = fork_and_send, args = (msg, ))
    thread.start()
