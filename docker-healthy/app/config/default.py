from os import environ

slack_token = str(environ['SLACK_TOKEN'])  # Auth toke to slack
slack_chanel = str(environ['SLACK_CHANNEL'])  # Slack post message channel
pager_routing_key = str(environ['PAGER_ROUTING_KEY'])  # Pager duty
