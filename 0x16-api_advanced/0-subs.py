#!/usr/bin/python3
""" Module for task 0 """
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'reddit_api:project:\(by /u/bekahabesha)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return 0
