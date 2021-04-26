import praw
import prawcore

reddit = praw.Reddit(
    client_id="<client-id>",
    client_secret="<client-secret>",
    user_agent="python:subtester:0.1 (by /u/ACEDT)",
)

def searchSubs(searchString):
    subList = []
    for sub in reddit.subreddits.search(searchString):
        subList.append(sub.display_name)
    return subList
def runner():
    subList = searchSubs("<search-string>")
    for sub in subList:
        print(sub)
runner()