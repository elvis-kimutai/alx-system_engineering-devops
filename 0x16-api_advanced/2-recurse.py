#!/usr/bin/python3
"""
   recursive function that queries the Reddit API and returns a list containing
   the titles of all hot articles for a given subreddit
"""

import requests

def get_hot_titles(subreddit, hot_list=[], after="", count=0):
    """
    Recursive function to retrieve titles of hot articles from
    a subreddit using the Reddit API.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check for a 404 error
    if response.status_code == 404:
        return None

    # Parse the JSON response
    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    # Extract titles from the response and add to the hot_list
    for child in data.get("children"):
        title = child.get("data").get("title")
        hot_list.append(title)

    # If there are more posts, make a recursive call
    if after is not None:
        return get_hot_titles(subreddit, hot_list, after, count)

    # Return the final list of hot titles
    return hot_list
