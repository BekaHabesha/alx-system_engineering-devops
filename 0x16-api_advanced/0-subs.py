#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API to get the subscriber count for a subreddit.

  Args:
      subreddit: The name of the subreddit (without the 'r/').

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'Your User Agent Name'}  # Replace with your unique user agent

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()
    return data.get('data', {}).get('subscribers', 0)  # Handle potential missing data
  except requests.exceptions.RequestException:
    # Handle any errors during the request
    return 0
  except KeyError:
    # Handle case where 'subscribers' key is missing in response
    return 0
