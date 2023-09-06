import tweepy

# Replace with your own Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter's API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Fetch tweets from a specific user
def fetch_tweets(username, count=10):
    try:
        user_tweets = api.user_timeline(screen_name=username, count=count)
        for tweet in user_tweets:
            print(f"{tweet.created_at} - {tweet.text}")
    except tweepy.TweepError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    username = input("Enter Twitter username: ")
    fetch_tweets(username)
