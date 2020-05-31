import json
import requests
import app.config.default as cfg

ROUTING_KEY = cfg.pager_routing_key  # Api key
INCIDENT_KEY = ""  # Incident key, may be null


def pager_trigger_incident(message):
    header = {
        "Content-Type": "application/json"
    }

    payload = {  # Payload
        "routing_key": ROUTING_KEY,
        "event_action": "trigger",
        "dedup_key": INCIDENT_KEY,
        "payload": {
            "summary": message,
            "source": "ec2",
            "severity": "critical"
        }
    }

    response = requests.post('https://events.pagerduty.com/v2/enqueue',
                             data=json.dumps(payload),
                             headers=header)

    if response.json()["status"] == "success":
        print('Incident Created')
    else:
        print(response.text)  # Print error


if __name__ == '__main__':
    pager_trigger_incident()
