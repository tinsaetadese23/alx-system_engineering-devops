#!/usr/bin/python3
"""Module for task 0"""


import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Total number of subscribers for the subreddit, or 0 if invalid.
    """
    try:
        # Set a custom User-Agent to avoid rate limits
        headers = {'User-Agent': 'MyRedditBot/1.0'}
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0  # Invalid subreddit or other error
    except Exception as e:
        print(f"Error fetching data: {e}")
        return 0

# Example usage:
subreddit_name = 'learnprogramming'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers in r/{subreddit_name}: {subscribers_count}")

