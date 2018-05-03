# Reddit Image Scraper

## Install instructions.
Replace the following with your reddit API information.
```
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='Image fetcher by J_C___',
                     username='')
```

Read into the 'image_fetch(already_fetched)' function to find the 'if' statement inside the only 'for' loop.
```
if submission.link_flair_text == 'Flair Text' and ("word1" in submission.title.lower() and "word2" in submission.title.lower()) and submission.id not in already_fetched:
```
You can customize this logic check to your liking. The "Flair Text" is the actual text seen inside a post's flair and word1 and word2 are the two words that you want to make sure are in the post title.
These conditions are completely optional but help narrow down your search!
