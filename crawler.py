#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id="4JSYiWXtv1n-1w", \
                     client_secret="44q49Vxj1ByRVm6r5ykb_EHbxbk", \
                     user_agent="Tess", \
                     username="Prettytess", \
                     password="legacy12.")

subreddit = reddit.subreddit('cscareerquestions').search("HireVue")
# top_subreddit = subreddit.top()
# top_subreddit = subreddit.search("HireVue")
# top_subreddit = subreddit.top(limit=2000)

for submission in reddit.subreddit('cscareerquestions').search("HireVue"):
    print()
    # print(submission.title, submission.id)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)
topics_data.to_csv('HireVue.csv', index=False)

# https://www.reddit.com/r/RWBYRP_Preview/
submissionid = []
comments = []

for submission in reddit.subreddit('cscareerquestions').search("HireVue"):
    submissionid.append(submission.id)

comments_dict = { "Submission_ID":[], \
                "Comments": []
                   }

replies_dict = { "Submission_ID":[], \
                "Replies": []
                   }

submission.comments.replace_more(limit=0)

for sub in submissionid:
    submit = reddit.submission(id = sub)
    for top_level_comment in submit.comments:
        comments_dict["Submission_ID"].append(submit)
        comments_dict["Comments"].append(top_level_comment.body)

comments_data = pd.DataFrame(comments_dict)
replies_data = pd.DataFrame(replies_dict)

comments_data.to_csv('CommentsHireVue.csv', index=False)
# replies_data.to_csv('RepliesHireVue.csv', index=False)