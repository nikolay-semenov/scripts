import docker
import requests
from app.notifications.slack import slack_post_message
from app.notifications.pager import pager_trigger_incident
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
metadata_request = requests.get('http://169.254.169.254/latest/meta-data/public-hostname')


def get_events():
    for events in client.events(decode=True):
        print(events)
        if events.get('status') is None:
            pass
        if events.get('status') == 'start':
            container_name = events['Actor']['Attributes']['name']
            message = "start container: " + container_name + " instance: " + metadata_request.text
            slack_post_message(message)
        if events.get('status') == 'kill':
            container_name = events['Actor']['Attributes']['name']
            message = "kill container: " + container_name + " instance: " + metadata_request.text
            slack_post_message(message=message)
            pager_trigger_incident(message=message)
        if events.get('status') == 'die':
            container_name = events['Actor']['Attributes']['name']
            message = "die container: " + container_name + " instance " + metadata_request.text
            slack_post_message(message=message)
            pager_trigger_incident(message=message)
        if events.get('status') == 'stop':
            container_name = events['Actor']['Attributes']['name']
            message = "stop container: " + container_name + " instance " + metadata_request.text
            slack_post_message(message=message)


get_events()
