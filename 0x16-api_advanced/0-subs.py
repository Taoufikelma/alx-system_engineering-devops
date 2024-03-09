import requests

def number_of_subscribers(subreddit):
    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.1'}  

    # URL for the subreddit's About page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Send GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Extract and return the number of subscribers
        return data['data']['subscribers']
    else:
        # Return 0 if the subreddit is invalid or request failed
        return 0
