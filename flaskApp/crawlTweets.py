import twint

class CrawlTweets():
    def __init__(self, username, numTweets):
        self.username = username
        self.numTweets = numTweets
        self.twintConfig = twint.Config()
        self.tweets = []

    def getTweets(self):
        self.twintConfig.Username = self.username
        self.twintConfig.Limit = self.numTweets
        self.twintConfig.Hide_output = True
        self.twintConfig.Store_object = True
        twint.run.Search(self.twintConfig)
        self.tweets = [obj.tweet for obj in twint.output.tweets_list]
        twint.output.tweets_list = []
        return self.tweets
