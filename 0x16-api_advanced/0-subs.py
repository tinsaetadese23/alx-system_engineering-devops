#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Total number of subscribers for the subreddit, or 0 if invalid.
    """
    import requests

    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "My-User-Agent"}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0  # Invalid subreddit or other error
    except Exception as e:
        print(f"Error fetching data: {e}")
        return 0

