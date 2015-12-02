#! /usr/local/bin/python
import requests
import json


# Global defaults
default_slack_endpoint = default_slack_channel = default_slack_name = default_slack_emoji = None

# Set defaults by writing a .slackbot file like:
#
# [SLACKBOT_DEFAULTS]
# ENDPOINT = https://hooks.slack.com/services/123/ABC
# CHANNEL = #random
# NAME = My Bot
# EMOJI = robot_face


def set_defaults():
    from configparser import ConfigParser
    from os.path import expanduser

    global default_slack_endpoint, default_slack_channel, default_slack_name, default_slack_emoji

    user_config_path = expanduser('~/.slackbot')
    config = ConfigParser()
    # Read config from local directory or home directory
    config.read(['./slackbot', user_config_path])

    default_slack_endpoint = config['SLACKBOT_DEFAULTS']['ENDPOINT']
    default_slack_channel = config['SLACKBOT_DEFAULTS']['CHANNEL']
    default_slack_name = config['SLACKBOT_DEFAULTS']['NAME']
    default_slack_emoji = config['SLACKBOT_DEFAULTS']['EMOJI']


def send_payload(message, channel, name, emoji, endpoint):
    payload = {
        "text": message,
        "channel": channel,
        "username": name,
        "icon_emoji": emoji,
    }
    payload_json = json.dumps(payload)
    response = requests.post(endpoint, data={"payload": payload_json})
    response.raise_for_status()


def notify_slack(message, channel='', name='', emoji='', endpoint=''):
    """
    Convenience method that normalizes payloads to Slack
    """
    if not endpoint and not default_slack_endpoint:
        set_defaults()

    channel = channel or default_slack_channel
    name = name or default_slack_name
    emoji = emoji or default_slack_emoji
    endpoint = endpoint or default_slack_endpoint

    # Normalize channel name
    if not channel.startswith('#') or channel.startswith('@'):
        channel = '#' + channel

    # Normalize :emoji:
    if not emoji.startswith(':'):
        emoji = ':%s:' % emoji

    send_payload(message, channel, name, emoji, endpoint)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        notify_slack(message=sys.argv[1])
    elif len(sys.argv) == 3:
        notify_slack(channel=sys.argv[1], message=sys.argv[2])
    elif len(sys.argv) == 5:
        notify_slack(name=sys.argv[1], emoji=sys.argv[2],
            channel=sys.argv[3], message=sys.argv[4])
    else:
        print("Usage: %s [[name emoji] channel] message" % sys.argv[0])
