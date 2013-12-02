#!/usr/bin/python
import os
from ConfigParser import ConfigParser
from twitter import Twitter, OAuth, TwitterHTTPError

notification_host_pager_body = u"""Host: {!s} ({!s}) IP:{!s}, State: {!s} -> {!s} ({!s})""".format(os.environ['NOTIFY_HOSTNAME'].replace('.','_'), os.environ['NOTIFY_HOSTALIAS'].replace('.','_'), os.environ['NOTIFY_HOSTADDRESS'], os.environ['NOTIFY_LASTHOSTSTATE'], os.environ['NOTIFY_HOSTSTATE'], os.environ['NOTIFY_NOTIFICATIONTYPE'])

notification_service_pager_body = u"""Host: {!s} ({!s}), IP: {!s}, Service: {!s} State: {!s} -> {!s} ({!s})""".format(os.environ['NOTIFY_HOSTNAME'].replace('.','_'), os.environ['NOTIFY_HOSTALIAS'].replace('.','_'), os.environ['NOTIFY_HOSTADDRESS'], os.environ['NOTIFY_SERVICEDESC'], os.environ['NOTIFY_LASTSERVICESTATE'], os.environ['NOTIFY_SERVICESTATE'], os.environ['NOTIFY_NOTIFICATIONTYPE'])

config = ConfigParser()
config.read(os.environ['TWITTER_CONFIG_FILE'])
conn = Twitter(auth=OAuth(config.get('default', 'oauth_token'), config.get('default', 'oauth_secret'), config.get('default', 'consumer_key'), config.get('default', 'consumer_secret')))

if os.getenv('NOTIFY_SERVICEDESC') is None:
    body_t = notification_host_pager_body
else:
    body_t = notification_service_pager_body

conn.direct_messages.new(user=os.environ['CONTACTPAGER'], text=body_t)
