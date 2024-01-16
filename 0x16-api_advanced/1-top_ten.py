#!/usr/bin/python3

"""
A function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
@authour: Bolakale Aduloju
"""

from requests import get


def top_ten(subreddit):
    """
   A function that queries the Reddit API and prints
   the titles of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
