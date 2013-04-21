from twitter import *
import re
import time
import sqlite3

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
        if('text' not in tweet.keys()):
            return False

        NumberResults = self.Regex.findall(tweet['text'])
        if(len(NumberResults) > 0):
            NumberResults = NumberResults[0]
        else:
            return False

        if(len(NumberResults) > 0):
            print tweet['user']['screen_name'] + " : " + tweet['text'] + " : " + str(NumberResults)
            self.addtodb(tweet['user']['screen_name'], NumberResults)


    def addtodb(self, username, number):

        Database = sqlite3.connect('database.db')
        DbCursor = Database.cursor()

        DbCursor.execute("CREATE TABLE IF NOT EXISTS TwitterNumbers (twittername VARCHAR(255), phone VARCHAR(255));")
        Database.commit()

        Insert = "INSERT INTO TwitterNumbers VALUES (?,?);"
        DbCursor.execute(Insert, (username, number))
        Database.commit()

        print Insert

        Database.commit()
        DbCursor.close()
        Database.close()

        print "Database Commited!"

if(__name__ == "__main__"):
    crawl = CrawlTwitNumbers()
    crawl.run()