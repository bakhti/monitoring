The script ```send2ses.py``` can be used to send check_mk notifications via AWS SES (Simple Email Service), so [Boto](https://github.com/boto/boto) package is required:

```bash
sudo pip install boto
```

IAM user credentials are taken from ```AWS_CONFIG_FILE``` file:

```bash
cat > ~/.aws_config << END
[default]
aws_access_key_id=
aws_secret_access_key=
```
The script ```send2twitter.py``` can be used to send check_mk notifications via Twitter. Python [twitter](https://github.com/sixohsix/twitter) package is required for the script to work:

```bash
sudo pip install simplejson requests requests_oauthlib twitter
```

The tikens and keys should be kept in ```TWITTER_CONFIG_FILE``` file:

```bash
cat > ~/.twitter_config << END
[default]
oauth_token=
oauth_secret=
consumer_key=
consumer_secret=
```

Both scripts take their config file path from environment variables:

```bash
cat > ~/etc/environment << END
AWS_CONFIG_FILE="$OMD_ROOT/.aws_config"
TWITTER_CONFIG_FILE="$OMD_ROOT/.twitter_config"
```