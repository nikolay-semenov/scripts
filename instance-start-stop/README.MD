### INFO

This script observes keys in redis. When the key value is changed, it makes a call in the AWS-API.

Calls available in / app / actions. So far, there are only two:

- instance_start: sends a call to run instace, waits for the status of running.

- insatnce_stop: sends a call to stop instace, waits for the status of stopping.

There is also a simple notifier, he notifies the slack of calls:

- script running

- instance start

- instance stop

- scrip stopping

- script error (so far, only as part of the exception aws client error)

### HOW TO

Dependencies are described in requirements.txt. Build occurs by tag, from the master branch.

The entire installation process is described in Dockerfile

On the infrastructure side, the following dependencies are required:

- At the initial initialization and deployment of the server part of the game - the presence of a list of keys, format network-name,application port (ex: network-1,80)

- Previously, mapping should be ready: network-name > instance-id

All this is done on the deployment side.

Container launch looks like this:

> docker run -itd --network host --name name --env <ALL NEED ENV> <IMAGE>

The following variables must be specified

- DEBUG='bool' - True or blank line. If blank then False

- DRY_RUN='bool' - True or blank line. If blank then False

- REDIS_HOST="sting" - cannot be empty. Host then where to be redis server

- REDIS_PORT=int - cannot be empty. Redis server port

- AWS_REGION="string" - cannot be empty. AWS region where are we running

- AWS_ACCESS_KEY="string" - access key for performing operations via api 

- AWS_SECRET_KEY="string" - secret key for performing operations via api

- SLACK_TOKEN="sting" - slack api token for send notification (In the future will be optional)

- SLACK_CHANNEL="#string" - slack channel for send notification (In the future will be optional)

