from flask import Flask
from flask import make_response, jsonify
from flask_restful import Resource, Api
import GetOldTweets3 as got

app = Flask(__name__)
api = Api(app)

class Tweets(Resource):
    def get(self, username):
        tweetCriteria = got.manager.TweetCriteria().setUsername("@MOH_Kenya")\
                                           .setMaxTweets(5)\
                                           .setTopTweets(True)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        text_tweets = [[tweet.date, tweet.text] for tweet in tweets]
        return make_response(jsonify(text_tweets), 200)

api.add_resource(Tweets, '/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)