import redis
import app.actions.ec2 as action
import app.config.default as cfg
from app.notifications.client import post_message_init
# State
state_active = "1"
state_inactive = "0"


# Redis
r = redis.Redis(host=cfg.redis_host, port=cfg.redis_port, db=0)
pub_sub = r.pubsub()
pub_sub.psubscribe('*:battleNetworkStatus')
post_message_init()

# Dicts
networks_state = {}
instance_state = {}


def start_network(network_name):
    print('starting network {}'.format(network_name))
    h_get_all = r.hgetall(name='mappingInstanceNetwork')
    for key, value in h_get_all.items():
        instance_state[key.decode("utf-8")] = value.decode("utf-8")
    action.instance_action_start(instance_id=[tuple(instance_state[network_name].split())])


def stop_network(network_name):
    print('stopping network {}'.format(network_name))
    h_get_all = r.hgetall(name='mappingInstanceNetwork')
    for key, value in h_get_all.items():
        instance_state[key.decode("utf-8")] = value.decode("utf-8")
    action.instance_action_stop(instance_id=[tuple(instance_state[network_name].split())])


def convert_hash_set(networks_state):
    result = new_d = {network.decode('utf-8'): state.decode('utf-8') for network, state in networks_state.items()}
    return result


def add_networks(old_state, new_state):
    for network, state in new_state.items():
        if network in old_state:
            continue
        old_state[network] = state
        if state == state_active:
            start_network(network)
        else:
            stop_network(network)


def update_networks(old_state, new_state):
    for network, state in new_state.items():
        if (not network in old_state) or (state == old_state[network]):
            continue
        old_state[network] = state
        if state == state_active:
            start_network(network)
        else:
            stop_network(network)


def remove_deleted_networks(old_state, new_state):
    for network in list(old_state.keys()):
        if network in new_state:
            continue
        state = old_state.pop(network, None)
        if state == state_active:
            stop_network(network)


while True:
    for m in pub_sub.listen():
        if cfg.debug:
            print(m)
        updated_networks_state = r.hgetall('battleNetworkStatus')
        updated_networks_state = convert_hash_set(updated_networks_state)
        if cfg.debug:
            print('old_state:')
            print(networks_state)
            print('new_state:')
            print(updated_networks_state)
        add_networks(networks_state, updated_networks_state)
        update_networks(networks_state, updated_networks_state)
        remove_deleted_networks(networks_state, updated_networks_state)
        if cfg.debug:
            print('old_state:')
            print(networks_state)
            print('new_state:')
            print(updated_networks_state)