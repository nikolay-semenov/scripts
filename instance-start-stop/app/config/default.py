from os import environ

debug = bool(environ['DEBUG'])  # Set debug log: False as blank
dry_run = bool(environ['DRY_RUN'])  # Set dry run: False as blank
redis_host = str(environ["REDIS_HOST"])  # Redis ip address
redis_port = int(environ["REDIS_PORT"])  # Redis port
aws_region = str(environ["AWS_REGION"])  # Running aws region
aws_access_key = str(environ["AWS_ACCESS_KEY"])  # Auth public key
aws_secret_key = str(environ["AWS_SECRET_KEY"])  # Auth secret key
slack_token = str(environ['SLACK_TOKEN'])  # Auth toke to slack
slack_chanel = str(environ['SLACK_CHANNEL'])  # Slack post message channel
