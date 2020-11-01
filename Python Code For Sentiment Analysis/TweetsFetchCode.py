import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'QHki2BEMao3yxvLqm2fyur4GRsV'
consumer_secret = '6jwS9trrhtICudeupvFheaa7SJVXzUPP2aYvytjYPFC3Dhwh6MlJ'
access_token = '949596312802009088-siYo0Ofzwdo2wJnTkXOreYstkKfZ5Qjg'
access_token_secret = 'O95sfhJgmy8wiiurmRJSYbWyuoIIPFL8icJt9U74di3qUJK'

csvFile = open('politicaltweetsmany.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
i=1;

  

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
tweets=tweepy.Cursor(api.search,q="#loksabhaelections2019",lang="en",geocode="20.5937,78.9629,1200km",count="100",since="2019-04-15",tweet_mode="extended").items(100000);

#csvWriter.writerow(["time","text","location","userid","screenname","retweetcount"])

for tweet in tweets:
   #print(i,tweet.full_text,tweet.user.location,tweet.user.id,tweet.user.screen_name);
   print(i)
   i=i+1;
   if(not tweet.retweeted) and ('RT @' not in tweet.full_text):
      csvWriter.writerow([tweet.created_at,tweet.full_text.encode('UTF-8'),tweet.user.location,tweet.user.id,tweet.user.screen_name,tweet.retweet_count])

#"19.6632,75.3002,100km"...maharashtra
#q="#modi"or "#bjp" or "#chowkidar" or "#namo" or "#modigovt" or "#modigovernment" or "#narendramodi namo,"
#12696 modi tweets..13463..chowkidarchor....rahulgandhi #rahulgandhi #bjp #india #congress #narendramodi #modi #politics #amitshah #indian #soniagandhi #election #rss #priyankagandhi #yogiadityanath #namo #inc #indianpolitics #rajasthan #gandhi #follow #indiannationalcongress #delhi #up #bollywood #madhyapradesh #pappu #chhattisgarh #memes #bjym #bhfyp.21800-congress
