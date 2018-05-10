# Reddit Image Scraper

## Install instructions.
Edit the auth.ini.example file to contain your credentials and save it as auth.ini

## IMPORTANT VARIABLES:
```
SUBREDDIT = "python"
word1 = ""
word2 = ""
flair = ""
```


Read into the 'image_fetch(already_fetched)' function to find the 'if' statement inside the only 'for' loop.
```
if submission.link_flair_text == flair and (word1 in submission.title.lower() and word2 in submission.title.lower()) and submission.id not in already_fetched:
```
You can customize this logic check to your liking. The words are meant to narrow your search results but they are optional.
