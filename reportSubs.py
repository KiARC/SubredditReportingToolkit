import praw
import prawcore
import SubredditTester

reddit = praw.Reddit(
    client_id="<client-id>",
    client_secret="<client-secret>",
    user_agent="python:subtester:0.1 (by /u/ACEDT)",
    password="<your-password>",
    username="<your-username>",
)

def reportSubs(subsActive, subsReporting):
    reason = input("Please briefly explain why you are reporting these subreddits: ")
    confirm = input("You are reporting " + str(subsReporting) + " subreddit(s) for \"" + reason + "\". Continue? (y/N): ")
    if confirm == "y":
        print("Okay, sending report message...")
    else:
        print("Cancelling report.")
        quit()
    message = "I am sending this message to report the following subreddit(s) for the following reason: " + reason + " \n\n" + '\n'.join([i for i in subsActive[0:]]) + "\nThank you for looking into this. \n\n^(This message was sent using PRAW but I do manually add subreddits to the list. I use this script to automatically report the list of subreddits I have compiled so that I can do so all at once rather than sending many individual reports.)"
    reddit.subreddit("reddit.com").message("Subreddit Report", message)
    reddit.redditor(username).message("Copy of Subreddit Report", message)
def runner():
    print("Obtaining list of active subs from the list...")
    subsActive = SubredditTester.runner(False)
    if len(subsActive) == 0:
        print("No active subreddits found!")
        quit()
    subsReporting = len(subsActive)
    print(str(subsReporting) + " active subreddit(s) found:\n" + 20*"=")
    for sub in subsActive:
        print(sub)
    print(20*"=")
    reportSubs(subsActive, subsReporting)
runner()