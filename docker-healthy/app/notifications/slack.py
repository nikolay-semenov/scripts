import app.config.default as cfg
from slack import WebClient
from slack.errors import SlackApiError


def slack_post_message(message):
    slack_chanel = cfg.slack_chanel
    slack_token = cfg.slack_token
    slack_client = WebClient(token=slack_token)
    try:
        message = slack_client.chat_postMessage(
            channel=slack_chanel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Docker event: " + message
                    }
                }
            ]
        )
    except SlackApiError as err:
        print(err)
