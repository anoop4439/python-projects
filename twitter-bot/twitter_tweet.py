import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # replace with actual tokens
auth.set_access_token(access_token, access_token_secret) # replace with actual tokens

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        return

# search_string = 'python'
# numberOfTweets = 2

### Code to like tweets with particular word ###

# for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         print(f"I liked that tweet")
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

### Code list the followers of the account ###

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    
    ### Code to follow the followers back ###
    # if follower.name == 'deepu':
    #     follower.follow()
    #     break