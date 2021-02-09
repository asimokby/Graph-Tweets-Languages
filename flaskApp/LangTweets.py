from fasttext import load_model
from crawlTweets import CrawlTweets
import emoji

class LangIdentifier():
    def __init__(self, username):
        self.username = username
        self.langs = {}
        crawlObj = CrawlTweets(self.username, 250)
        self.textTweets = crawlObj.getTweets()
    def loadModel(self):
        return load_model("lid.176.ftz") 

    def detectLang(self, text):
        return self.lid_model.predict(text)

    def remove_emoji(self, text):
        return emoji.get_emoji_regexp().sub(u'', text)

    def cleanTweets(self):
        self.textTweets = [' '.join([word for word in tweet.split(' ') 
        if '#' not in word and '@' not in word and 'http' not in word
        and 'pic.twitter.com' not in word])for tweet in self.textTweets]
        
        self.textTweets = [self.remove_emoji(tweet.replace('\n', '').lower()) for tweet in self.textTweets]

    def getLangs(self):  
        if len(self.textTweets) == 0:
            return -1 
        self.cleanTweets()
        self.lid_model = self.loadModel()
        for tweet in self.textTweets:
            if len(tweet) < 20:
                continue 
            lang = self.detectLang(tweet)
            langCode = lang[0][0].split('__')[-1]
            langAcc = lang[1][0]
            if langAcc > 0.6:
                if langCode not in self.langs:
                    self.langs[langCode] = 1
                else: 
                    self.langs[langCode] += 1
        return self.langs 

