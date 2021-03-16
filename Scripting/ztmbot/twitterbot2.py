import tweepy
import time

auth = tweepy.OAuthHandler('GZWVNKLCJ6PBzt8rql1kqWGdY', 'd7E1ab0nibe8nS35M4bHien7R2NhkEeaBX0QtRdwlItmqrZ0yz')
auth.set_access_token('632288942-YPTl36mulk5XRyGcriPFeGlz0fAihxmSFoudTPaQ',
                      'KXE87VPj1278zBmVuh04ELDoX5S3DrwkQYo0GpUTNnGOD')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


try:
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name =='anudeep':
            follower.follow()
            break
        print(follower.name)
except RuntimeError:
    print('End of follower list')