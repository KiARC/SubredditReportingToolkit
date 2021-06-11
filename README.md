# SubredditReportingToolkit
A set of python scripts to find and report subreddits.

# How to use the toolkit:
### Setup:
- Use [this guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#python-example) to set up a "script" on your profile
- Fill in this section of the script with your information by replacing <client-id> and <client-secret> with your id and secret.
```python 
reddit = praw.Reddit(
    client_id="<client-id>",
    client_secret="<client-secret>",
    user_agent="python:subtester:0.1 (by /u/ACEDT)",
)
 ```
 - Add your Reddit username and password to `reportSubs`
 - Follow the instructions to use it!


### Basic step-by-step:
- Find subreddits with `SubFinder`
- Check them manually, it will not necessarily only find things you want to report! (For example, the search term "homophobic" will still register r/LGBT because there are posts/content there including that word.)
- Add them to a file `sublist.txt`
- Run `SubredditTester` to confirm their statuses. You can keep banned subs there to keep track of them!
- Run `reportSubs` to send the report message.
