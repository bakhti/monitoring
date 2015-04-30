#!/usr/bin/python
from os import environ, getenv
from ConfigParser import ConfigParser
from twitter import Twitter, OAuth

notification_host_pager_body = u"""
Host: {!s} ({!s}) IP:{!s}, State: {!s} -> {!s} ({!s})
""".format(
    environ['NOTIFY_HOSTNAME'].replace('.', '_'),
    environ['NOTIFY_HOSTALIAS'].replace('.', '_'),
    environ['NOTIFY_HOSTADDRESS'],
    environ['NOTIFY_LASTHOSTSTATE'],
    environ['NOTIFY_HOSTSTATE'],
    environ['NOTIFY_NOTIFICATIONTYPE'])

notification_service_pager_body = u"""
Host: {!s} ({!s}), IP: {!s}, Service: {!s} State: {!s} -> {!s} ({!s})
""".format(
    environ['NOTIFY_HOSTNAME'].replace('.', '_'),
    environ['NOTIFY_HOSTALIAS'].replace('.', '_'),
    environ['NOTIFY_HOSTADDRESS'],
    environ['NOTIFY_SERVICEDESC'],
    environ['NOTIFY_LASTSERVICESTATE'],
    environ['NOTIFY_SERVICESTATE'],
    environ['NOTIFY_NOTIFICATIONTYPE'])

config = ConfigParser()
config.read(environ['TWITTER_CONFIG_FILE'])
conn = Twitter(auth=OAuth(config.get('default', 'oauth_token'),
                          config.get('default', 'oauth_secret'),
                          config.get('default', 'consumer_key'),
                          config.get('default', 'consumer_secret')))

if getenv('NOTIFY_SERVICEDESC') is None:
    body_t = notification_host_pager_body
else:
    body_t = notification_service_pager_body

conn.direct_messages.new(user=environ['CONTACTPAGER'], text=body_t)
