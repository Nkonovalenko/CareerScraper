#! python3
import praw # Python Reddit API Wrapper
import pandas as pd
import datetime as dt

def get_date(created):
	return dt.datetime.fromtimestamp(created)


reddit = praw.Reddit(client_id='CLIENT_ID', \
					 client_secret = 'SECRET_CODE', \
					 user_agent = 'Scrape', \
					 username = 'REDDIT USERNAME', \
					 password = 'REDDIT_PASSWORD')

subreddit = reddit.subreddit('cscareerquestions')


top_subreddit = subreddit.top(limit = 50)
new_subreddit = subreddit.new(limit = 50)

amazon_subreddit = subreddit.search("amazon")
google_subreddit = subreddit.search("google")
microsoft_sub = subreddit.search("microsoft")
intern_subreddit = subreddit.search("intern")

for thread in subreddit.top(limit=1):
	print(thread.title, thread.id)

topics_dict = { "title": [], \
				"score": [], \
				"id": [], "url":[], \
				"comms_num": [], \
				"created": [], \
				"body":[]}


for thread in subreddit.top():
	topics_dict["title"].append(thread.title)
	topics_dict["score"].append(thread.score)
	topics_dict["id"].apppend(thread.id)
	topics_dict["url"].append(thread.url)
	topics_dict["comms_num"].append(thread.num_comments)
	topics_dict["created"].append(thread.created)
	topics_dict["body"].append(thread.body)

topics_data = pd.DataFrame(topics_dict)

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)


topics_data.to_csv('CS_Scrape.csv', index = False)