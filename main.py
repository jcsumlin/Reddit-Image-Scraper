# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:13:40 2018

@author: Chat
"""
import praw
import os
from urllib import request
import configparser 
import ast
config = configparser.ConfigParser()
config.read('config.ini')


reddit = praw.Reddit(client_id=config['default']['client_id'],
                     client_secret=config['default']['client_secret'],
                     password=config['default']['password'],
                     user_agent=config['default']['user_agent'],
                     username=config['default']['username'])

print("Account logged in: ", reddit.user.me())
SUBREDDIT = str(config['default']['SUBREDDIT'])
flair = str(config['default']['Flair'])
filter_words = ast.literal_eval(config['default']['filter_words'])
LIMIT = int(config['default']['LIMIT'])

if not os.path.isfile("already_fetched.txt"):
    already_fetched = []
else:
    with open("already_fetched.txt", "r") as f:
       already_fetched = f.read()
       already_fetched = already_fetched.split("\n")
       already_fetched = list(filter(None, already_fetched))
       
def image_fetch(already_fetched, flair, filter_words):
    subreddit = reddit.subreddit(SUBREDDIT)
    new_posts = subreddit.new(limit=LIMIT)
    for submission in new_posts:
        if submission.link_flair_text == flair and (filter_word_check(filter_words, submission.title)) and submission.id not in already_fetched:
            url = submission.url
            try:
                f = open(str(submission.author)+".jpg", 'wb')
                f.write(request.urlopen(url).read())
                f.close()   
            except:
                print("Silently Failing. Can't save file")
            already_fetched.append(submission.id)
    with open("already_fetched.txt", "w") as f:
        for x in already_fetched:
            f.write(x + "\n")
            
def filter_word_check(filter_words, title):
    for x in filter_words:
        if x in title.lower():
            return True
        else:
            return False
image_fetch(already_fetched, flair, filter_words)
    