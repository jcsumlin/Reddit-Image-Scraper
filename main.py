# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:13:40 2018

@author: Chat
"""
import praw, os
from urllib import request

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='Image fetcher by J_C___',
                     username='')

print("Account logged in: ", reddit.user.me())
SUBREDDIT = "all"


if not os.path.isfile("already_fetched.txt"):
    already_fetched = []
else:
    with open("already_fetched.txt", "r") as f:
       already_fetched = f.read()
       already_fetched = already_fetched.split("\n")
       already_fetched = list(filter(None, already_fetched))
       
def image_fetch(already_fetched):
    subreddit = reddit.subreddit(SUBREDDIT)
    posts = subreddit.new(limit=500)
    for submission in posts:
        if submission.link_flair_text == 'Flair Text' and ("word1" in submission.title.lower() and "word2" in submission.title.lower()) and submission.id not in already_fetched:
            print(submission.title)
            url = submission.url
#            pic = re.search('(i.redd.it)\W(\w{1,}.jpg)', url).group(2)
            f = open(str(submission.title)+".jpg", 'wb')
            f.write(request.urlopen(url).read())
            f.close()                
#            submission.upvote()
            already_fetched.append(submission.id)
try:
    image_fetch(already_fetched)
except KeyboardInterrupt:
    with open("already_fetched.txt", "w") as f:
        for x in already_fetched:
            f.write(x + "\n")