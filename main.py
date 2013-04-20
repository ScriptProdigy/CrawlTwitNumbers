from twitter import *
import re
import time

class CrawlTwitNumbers:
    def __init__(self):

        self.Regex_Pattern = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
        self.Regex = re.compile(self.Regex_Pattern)

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

            Numbers = ""
            NumberResults = self.Regex.findall(tweet['text'])
            
            for number in NumberResults:
                Numbers += number + " "


            if(len(NumberResults) > 0):
                print tweet['user']['screen_name'] + " : " + tweet['text'] + " : " + str(Numbers)

        except:
            pass

    def addtodb(self, username, number):
        pass

if(__name__ == "__main__"):
    crawl = CrawlTwitNumbers()
    crawl.run()