This simple script monitors start, stop, kill, die events. And sends notifications to the slack. For events, die is also used pager durty.

Required variables:

- SLACK_TOKEN="xoxb-xxx-yyy-zzz" 

- SLACK_CHANNEL="#channel-name" 

- PAGER_ROUTING_KEY="ABCDEFG"

Other dependencies: -v /var/run/docker.sock:/var/run/docker.sock

Example usage: docker run -itd --network host -v /var/run/docker.sock:/var/run/docker.sock --env SLACK_TOKEN="xoxb-key" --env SLACK_CHANNEL="#channel" --env PAGER_ROUTING_KEY="PG-KEY" image
