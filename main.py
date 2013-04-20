from twitter import *
import time

class CrawlTwitNumbers:
    def __init__(self):

        UserPassFile = open("twitter_account.txt", "r").read()
        Username = str(UserPassFile.split(":")[0])
        Password = str(UserPassFile.split(":")[1].rstrip())

        self.TwitterAuth = UserPassAuth(Username, Password)
        self.Stream = TwitterStream(auth=self.TwitterAuth)

        self.StreamIterator = self.Stream.statuses.sample()

    def run(self):
        for tweet in self.StreamIterator:
            self.processTweet(tweet)


    def processTweet(self, tweet):
        try:
            print ""
            print tweet['user']['screen_name'] + " : " + tweet['text']
            print ""
        except:
            pass

    def addtodb(self, username, number):
        print username + "'s number is " + number

if(__name__ == "__main__"):
    crawl = CrawlTwitNumbers()
    crawl.run()