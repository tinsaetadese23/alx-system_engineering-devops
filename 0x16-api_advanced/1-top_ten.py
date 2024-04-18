#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {"User-Agent": "My-Reddit-Bot"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")  # Invalid subreddit or other error
    except Exception as e:
        print(f"Error fetching data: {e}")
