import boto3
import botocore.exceptions
import app.config.default as cfg
from app.notifications.client import post_message_instance_start, post_message_instance_stop, post_message_script_error


ec2_client = boto3.client('ec2',
                          region_name=cfg.aws_region,
                          aws_access_key_id=cfg.aws_access_key,
                          aws_secret_access_key=cfg.aws_secret_key)


def instance_action_start(instance_id):
    try:
        for instance in instance_id:
            response = ec2_client.start_instances(InstanceIds=instance, DryRun=cfg.dry_run)
            waiter = ec2_client.get_waiter('instance_running')
            waiter.wait(InstanceIds=instance)
            post_message_instance_start(instance_id=instance)
            print("Response:", response)
            print("Waiter:", waiter)
    except botocore.exceptions.ClientError as error:
        post_message_script_error(error=error)
        raise error


def instance_action_stop(instance_id):
    try:
        for instance in instance_id:
            response = ec2_client.stop_instances(InstanceIds=instance, DryRun=cfg.dry_run)
            waiter = ec2_client.get_waiter('instance_stopped')
            waiter.wait(InstanceIds=instance)
            post_message_instance_stop(instance_id=instance)
            print("Response:", response)
            print("Waiter:", waiter)
    except botocore.exceptions.ClientError as error:
        post_message_script_error(error=error)
        raise error
