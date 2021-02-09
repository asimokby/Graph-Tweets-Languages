from flask import Flask, render_template, request, jsonify     
import json 
from flask_cors import CORS
from LangTweets import LangIdentifier 

app = Flask(__name__)            
CORS(app)


@app.route('/process', methods=['GET','POST'])  
def process(): 
    if request.method == 'GET':
        return '<p>You lost? -_- Go back to the website from <a href="https://asimokby.github.io/Graph-Tweets-Languages/">here!</a><p>'
    # username = json.loads(request.data)['username']
    # if username.startswith('@'): username = username[1:]
    # langTweet = LangIdentifier(username)
    # langFreqDict = langTweet.getLangs()

    # if not langFreqDict == -1:
    #     return json.dumps(langFreqDict)
    # return jsonify({'error':'An error ocurred!'})

if __name__ == "__main__":        
    app.run()                     