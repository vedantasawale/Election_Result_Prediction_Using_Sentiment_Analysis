from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('menu.html')
 

@app.route('/compare.html')
def compare():
 return render_template('compare.html')

@app.route('/country.html')
def country():
 return render_template('country.html')

@app.route('/state.html')
def state():
 return render_template('state.html')

@app.route('/menu.html')
def menu():
 return render_template('menu.html')




@app.route('/live.html')
def live():
 return render_template("live.html")


@app.route('/stateresult.html',methods = ['POST', 'GET'])
def stateresult():
 url=""
 if request.method == 'POST':
    result = request.form
    for key, value in result.items():
     k=key
     state=""+value
 if state=="andhrapradesh":
    link='/static/andhrapradesh.png'
 elif state=="arunachalpradesh":
    link='/static/arunachalpradesh.png'
 elif state=="assam":
    link='/static/assam.png'
 elif state=="bihar":
    link='/static/bihar.png'
 elif state=="chandigarh":
    link='/static/chandigarh.png'
 elif state=="delhi":
    link='/static/delhi.png'
 elif state=="gujarat":
    link='/static/gujarat.png'
 elif state=="karnataka":
    link='/static/karnataka.png'
 elif state=="madhyapradesh":
    link='/static/madhyapradesh.png'
 elif state=="maharashtra":
    link='/static/maharashtra.png'
 elif state=="punjab":
    link='/static/punjab.png'
 elif state=="rajasthan":
    link='/static/rajasthan.png'
 elif state=="tamilnadu":
    link='/static/tamilnadu.png'
 elif state=="uttarpradesh":
    link='/static/uttarpradesh.png'
 elif state=="karnataka":
    link='/static/karnataka.png'     

 return render_template('stateresult.html',url=link)
 




@app.route('/liveresult.html',methods = ['POST', 'GET'])
def liveresult():
 if request.method == 'POST':
    result = request.form
    for key, value in result.items():
     k=key
     query=""+value
 import tweepy
 import pandas as pd
 import re
 import nltk
 #nltk.download('wordnet')
 #nltk.download('stopwords')
 from nltk.corpus import stopwords
 from nltk.stem.porter import PorterStemmer
 from textblob import TextBlob
 ####input your credentials here
 consumer_key = 'QHki2BEMao3yxvLqtrm2fr4GRsV'
 consumer_secret = '6jwS9rhtICudeurdpvFheaa7SJVXzUPP2aYvytjYPFC3Dhwh6MlJ'
 access_token = '9495963128020090yu88-sYo0Ofzwdo2wJnTkXOreYstkKfZ5Qjg'
 access_token_secret = 'O95sfhJgmy8dzwirmRJSYbWyuoIIPFL8icJt9U74di3qUJK'



 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)
 api = tweepy.API(auth,wait_on_rate_limit=True)
 tweets=tweepy.Cursor(api.search,q=query,lang="en",geocode="21.76,78.87,1500km",count="100",tweet_mode="extended").items(300);
 p=0
 n=0
 for tweet in tweets:
    #print(i,tweet.full_text,tweet.user.location,tweet.user.id,tweet.user.screen_name);
    tweet=tweet.full_text
    tweet = re.sub(r"http\S+", "", tweet)
    # print(tweet)
    #removing  emojis and n
    tweet = re.sub(r"#[a-zA-Z0-9]+", "", tweet)
    tweet = re.sub(r"\\x[a-zA-Z0-9]+", "", tweet)
    tweet = re.sub(r"\\n", " ", tweet)
    tweet = re.sub('[^a-zA-Z]', ' ', tweet)
    tweet = re.sub(r"\W"," ",tweet)
    tweet = re.sub(r"\d"," ",tweet)
    tweet = re.sub(r"s+[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+[a-z]$"," ",tweet)
    tweet = re.sub(r"^[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+"," ",tweet)
    tweet = tweet.lower()
    tweet = tweet.split()
    ps = PorterStemmer()
    tweet = [ps.stem(word) for word in tweet if not word in set(stopwords.words('english'))]
    tweet = ' '.join(tweet)
    score = TextBlob(tweet)
    
    if(score.sentiment.polarity<0):
        n=n+1
    elif(score.sentiment.polarity>0):
        p=p+1
 ppercent=int((p/(p+n))*100)
 npercent=int((n/(p+n))*100)
 import matplotlib.pyplot as plt
 fig=plt.figure(figsize=(8,6))
 names=["BJP","Congress"]
 scores=[ppercent]
 scores1=[npercent]
 positions=[0.5]
 positions1=[0.8]
 #positions2=[0.15,1.15]
 plt.bar(positions,scores,width=0.3,color="g",label="+ve sentiment")
 plt.bar(positions1,scores1,width=0.3,color="r",label="-ve sentiment")
 #plt.xticks(positions2,names)
 plt.title("Comparison of Sentiments")
 plt.ylabel("sentiment percentage")
 plt.xlabel("Parties")
 #plt.text()
 #plt.legend()
 plt.plot()
 plt.savefig("static/livepic.png")

 return render_template('finallive.html',url ='/static/livepic.png')
 


if __name__ == '__main__':
   app.run()
