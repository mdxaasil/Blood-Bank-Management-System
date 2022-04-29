import tweepy

consumer_key='fchmmSWvEXFMAjjx4RZNKqHbK'
consumer_secret='SkR4lCxbxTvb9cLL9uODN8DiGFxyyYCeZNFJj4l5eLMUKhBn61'
access_token='1343258269628788736-jyrUwlRLelsRKC1fzDxFHZVbEu9Mrk'
access_token_secret='Ox8AQXgP4Y0vCYdR4QkgFiPDb9UIw20qntrcjvKYZXmzC'

def OAuth():
    try:
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth

    except Exception as e:
        return None

oauth=OAuth()
api=tweepy.API(oauth)

cont=""" We need A+,B+ group blood for an 
emergency case at GD Hospital, . If you are willing to be a donor, please reply to this message as
soon as possible.

Contact Details: 9823815628

Kind regards,
GD Blood bank technician.  """

api.update_status(cont)

print("Tweet sent")