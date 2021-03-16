import tweepy

auth = tweepy.OAuthHandler('GZWVNKLCJ6PBzt8rql1kqWGdY', 'd7E1ab0nibe8nS35M4bHien7R2NhkEeaBX0QtRdwlItmqrZ0yz')
auth.set_access_token('632288942-YPTl36mulk5XRyGcriPFeGlz0fAihxmSFoudTPaQ', 'KXE87VPj1278zBmVuh04ELDoX5S3DrwkQYo0GpUTNnGOD')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)
print('\n')
for tweet in public_tweets:
    print(tweet.text)