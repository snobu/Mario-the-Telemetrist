# Init Application Insight clients
from applicationinsights import TelemetryClient
import datetime
import sys
from threading import Thread
from blessings import Terminal

# Read Application Insights instrumentation key into instrum_key
# (Cheap workaround to not store secrets in GitHub)
with open('data/telemetry/key_ai', 'r') as secret:
    instrum_key = secret.read().replace('\n', '')

tc = TelemetryClient(instrum_key)
t = Terminal()

def send_custom_event(msg):
    tc.track_event(msg)
    tc.flush()
    print 'Event {t.magenta}{msg}{t.normal} sent to {t.yellow}{t.bold}App Insights{t.normal}'.format(t=t, msg=msg)
    return True

def send_exception_event(type, value, tb):
    tc.track_exception(type=type, value=value, tb=tb)
    tc.flush()
    print 'Exception sent to {t.yellow}{t.bold}App Insights{t.normal}'.format(t=t)
    return True

def send_event_async(msg):
    thread = Thread(target = send_custom_event, args = (msg, ))
    thread.start()

def send_exception_async(type, value, tb):
    thread = Thread(target = send_exception_event, args = (type, value, tb, ))
    thread.start()
