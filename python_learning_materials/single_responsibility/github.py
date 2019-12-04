import urllib2
import json
import sys
import os
import logging

log_level = os.environ['LOG_LEVEL'] if os.environ.has_key('LOG_LEVEL') else "INFO"
logging.basicConfig(level=log_level, filename='output.log', format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)

if not os.environ.has_key('TOKEN'):
    print("TOKEN needs to be set to your github auth token")
    logger.fatal("Exiting because TOKEN was not set")
    sys.exit(1)
else:
    logger.debug("Using auth token: %s", os.environ['TOKEN'])

base_url = "https://github.wwt.com/api/v3"
logger.debug("Using base url: %s", base_url)

usernames = []

while True:
    try:
        username = raw_input('What user would you like to lookup? ')
        if username:
            usernames += [username]
            logger.debug("Received user: %s", username)
        else:
            break
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)


print("Github user's activities: %s" % ", ".join(usernames))

for username in usernames:
    url = base_url + "/users/%s/events" % username
    token = os.environ['TOKEN']
    authorization = "token %s" % token
    auth_headers = { 'Authorization': authorization }

    request = urllib2.Request(url, headers=auth_headers)

    try:
        response = urllib2.urlopen(request)
        response_data = json.loads(response.read())

        logger.info("Successfully fetching github events for: %s", username)
        print("  -> activities for %s:" % username)

        for event in response_data:
            repo_name = event['repo']['name']
            created_at = event['created_at']
            event_type = event['type']

            print("    -> %s - %s - %s" % (created_at, event_type, repo_name))
    except urllib2.HTTPError as error:
        logger.error("Couldn't fetch: %s", username)

