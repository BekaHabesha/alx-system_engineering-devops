#!/usr/bin/python3
#
# Script Name: getRedditJSONSubmissionData.py
# Usage: ./getRedditJSONSubmissionData.py > redditData.json
# ----------------------------------------------------------------------------------------------------------------
# This script will average one request every two seconds.  If the servers return data faster, you might
# need to change the sleep time to avoid going over the API limits.  
# Also, make sure you change the settings in your Reddit account to get 100 objects at a time.  You can
# also use the URL variable "limit=100" (it might be count=100?)
#
# Also, the code to handle errors if a non-status 200 response is received should be improved to 
# eventually stop requesting after X amount of failures -- this might happen if Reddit's servers go down
# for an extended time period.
# ----------------------------------------------------------------------------------------------------------------

import requests
import json
import time
import sys

user_pass_dict = {'user': 'your_user_name',
              'passwd': 'your_password',
              'api_type': 'json'}
s = requests.Session()
s.headers.update({'User-Agent' : 'short_description_of_yourself user:your_user_name'})
r = s.post(r'http://www.reddit.com/api/login', data=user_pass_dict)
j = json.loads(r.content)
after = "" # Set this to a T3 object to start at a specific point or leave blank to start with the most recent submissions

while True:
    time.sleep(1) # Sleep for one second to avoid going over API limits
    url = "http://www.reddit.com/r/all/new/.json?limit=100&after=" + after
    html = s.get(url) # Make request to Reddit API
    if html.status_code != 200:  # This error handing is extremely basic.  Please improve.
        # Error handing block
        sys.stderr.write(str(html.status_code)) # Print HTTP error status code to STDOUT
        sys.stderr.write(url)
        continue
        # End Error handling block
    print html.content # Print the JSON object 
    after = decode['data']['after']  # Update after variable to receive the next batch of submissions in this loop
