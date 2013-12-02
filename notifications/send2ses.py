#!/usr/bin/python
import os
from ConfigParser import ConfigParser
import boto.ses

notification_host_subject = u"[EU-MON] {!s} {!s}".format(os.environ['NOTIFY_HOSTNAME'], os.environ['NOTIFY_NOTIFICATIONTYPE'])
notification_service_subject = u"[EU-MON] {!s}/{!s} {!s}".format(os.environ['NOTIFY_HOSTNAME'], os.environ['NOTIFY_SERVICEDESC'], os.environ['NOTIFY_NOTIFICATIONTYPE'])

notification_common_body = u"""Host:     {!s}
Alias:    {!s}
Address:  {!s}
""".format(os.environ['NOTIFY_HOSTNAME'], os.environ['NOTIFY_HOSTALIAS'], os.environ['NOTIFY_HOSTADDRESS'])

notification_host_body = u"""State:    {!s} -> {!s} ({!s})
Command:  {!s}
Output:   {!s}
Perfdata: {!s}
{!s}
""".format(os.environ['NOTIFY_LASTHOSTSTATE'], os.environ['NOTIFY_HOSTSTATE'], os.environ['NOTIFY_NOTIFICATIONTYPE'], os.environ['NOTIFY_HOSTCHECKCOMMAND'], os.environ['NOTIFY_HOSTOUTPUT'], os.environ['NOTIFY_HOSTPERFDATA'], os.environ['NOTIFY_LONGHOSTOUTPUT'])

notification_service_body = u"""Service:  {!s}
State:    {!s} -> {!s} ({!s})
Command:  {!s}
Output:   {!s}
Perfdata: {!s}
{!s}
""".format(os.environ['NOTIFY_SERVICEDESC'], os.environ['NOTIFY_LASTSERVICESTATE'], os.environ['NOTIFY_SERVICESTATE'], os.environ['NOTIFY_NOTIFICATIONTYPE'], os.environ['NOTIFY_SERVICECHECKCOMMAND'], os.environ['NOTIFY_SERVICEOUTPUT'], os.environ['NOTIFY_SERVICEPERFDATA'], os.environ['NOTIFY_LONGSERVICEOUTPUT'])

config = ConfigParser()
config.read(os.environ['AWS_CONFIG_FILE'])
conn = boto.ses.SESConnection(config.get('default', 'aws_access_key_id'), config.get('default', 'aws_secret_access_key'))

if os.getenv('NOTIFY_SERVICEDESC') is None:
    subject_t = notification_host_subject
    body_t = notification_host_body
else:
    subject_t = notification_service_subject
    body_t = notification_service_body

conn.send_email('omdeu_noreply@runashop.com', subject_t, body_t, u"{!s} <{!s}>".format(os.environ['NOTIFY_CONTACTNAME'], os.environ['NOTIFY_CONTACTEMAIL']))
