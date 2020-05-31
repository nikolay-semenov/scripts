from slack import WebClient
from slack.errors import SlackApiError
from app.config.default import slack_chanel, slack_token


client = WebClient(token=slack_token)


def post_message_init():
    try:
        message = client.chat_postMessage(
            channel=slack_chanel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Run instance start\stop script"
                    }
                }
            ]
        )
    except SlackApiError as err:
        print(err)


def post_message_stop():
    try:
        message = client.chat_postMessage(
            channel=slack_chanel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Stop instance start\stop script"
                    }
                }
            ]
        )
    except SlackApiError as err:
        print(err)


def post_message_instance_start(instance_id):
    try:
        message = client.chat_postMessage(
            channel=slack_chanel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Instance start: " + str(instance_id)
                    }
                }
            ]
        )
    except SlackApiError as err:
        print(err)


def post_message_instance_stop(instance_id):
    try:
        message = client.chat_postMessage(
            channel=slack_chanel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Instance stop: " + str(instance_id)
                    }
                }
            ]
        )
    except SlackApiError as err:
        print(err)


def post_message_script_error(error):
    try:
        message = client.chat_postMessage(
            channel=slack_chanel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Container down, error: " + str(error)
                    }
                }
            ]
        )
    except SlackApiError as err:
        print(err)

