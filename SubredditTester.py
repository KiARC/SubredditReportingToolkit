import praw
import prawcore

reddit = praw.Reddit(
    client_id="<client-id>",
    client_secret="<client-secret>",
    user_agent="python:subtester:0.2 (by /u/ACEDT)",
)

def subExists(sub):
    exists = 0
    try:
        subtest = reddit.subreddit(sub)
        testvar = subtest.id
    except prawcore.exceptions.Redirect:
        exists = 1
    except prawcore.exceptions.NotFound:
        exists = 2
    except prawcore.exceptions.Forbidden:
        exists = 3
    return exists 
def readList(inFilePath):
    with open(inFilePath, 'r') as infile:
        subs = []
        for line in infile:
            line = line.replace("\n","")
            line = line.replace("r/","",1)
            line = line.split(' !', 1)[0] #Allows use of ! to add a comment in the sublist for readability
            subs.append(line)
    return subs
def outputResults(subs, printSubs):
    subsActive = []
    subsPrivate = []
    subsBanned = []
    subsMissing = []
    for sub in subs:
        sub = sub.lower()
        status = subExists(sub)
        if status == 0:
            if printSubs:
                print("Subreddit " + sub + " is active.")
            subsActive.append(sub)
        elif status == 1:
            if printSubs:
                print("Subreddit " + sub + " does not exist.")
            subsMissing.append(sub)
        elif status == 2:
            if printSubs:
                print("Subreddit " + sub + " has been banned.")
            subsBanned.append(sub)
        elif status == 3:
            if printSubs:
                print("Subreddit " + sub + " has been made private.")
            subsPrivate.append(sub)
    subsActive = ["r/" + sub + "\n" for sub in subsActive]
    subsPrivate = ["r/" + sub + "\n" for sub in subsPrivate]
    subsBanned = ["r/" + sub + "\n" for sub in subsBanned]
    subsMissing = ["r/" + sub + "\n" for sub in subsMissing]
    return subsActive, subsPrivate, subsBanned, subsMissing
def logData(logFilePath, subsActive, subsPrivate, subsBanned, subsMissing):
    with open(logFilePath,"w") as logFile:
        logFile.write("Subreddits that are active as of this test:\n|" + 23*"=" + "|\n")
        logFile.writelines(subsActive)
        logFile.write("|" + 23*"=" + "|\nSubreddits that are private as of this test:\n|" + 23*"=" + "|\n")
        logFile.writelines(subsPrivate)
        logFile.write("|" + 23*"=" + "|\nSubreddits that are banned as of this test:\n|" + 23*"=" + "|\n")
        logFile.writelines(subsBanned)
        logFile.write("|" + 23*"=" + "|\nSubreddits that were not found during this test:\n|" + 23*"=" + "|\n")
        logFile.writelines(subsMissing)
        logFile.write("|" + 23*"=" + "|")
def runner(printSubs =True):
    subs = readList('sublist.txt')
    subsActive, subsPrivate, subsBanned, subsMissing = outputResults(subs, printSubs)
    logData('SubredditTestLog.txt', subsActive, subsPrivate, subsBanned, subsMissing)
    return subsActive, subsPrivate
if __name__ == "__main__":
    runner()
