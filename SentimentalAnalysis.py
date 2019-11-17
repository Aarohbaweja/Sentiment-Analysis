# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from textblob import TextBlob
import sys , tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)
#Enter Keys
consumerKey=""
consumerSecret=""
accessToken=""
accessTokenSecret=""

auth= tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api=tweepy.API(auth)

searchTerm=input("Enter keyword/hashtag to search about:")
noOfTweets=int(input("Enter no. of tweets to analyze:"))

tweets=tweepy.Cursor(api.search,q=searchTerm,lang="en").items(noOfTweets)

polarity = 0
positive = 0
wpositive = 0
spositive = 0
negative = 0
wnegative = 0
snegative = 0
neutral = 0

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
         neutral += 1
    elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
          wpositive += 1
    elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
           positive += 1
    elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
         spositive += 1
    elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
          wnegative += 1
    elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
    elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1

  # finding average of how people are reacting
positive =percentage(positive, noOfTweets)
wpositive =percentage(wpositive, noOfTweets)
spositive =percentage(spositive, noOfTweets)
negative =percentage(negative, noOfTweets)
wnegative =percentage(wnegative, noOfTweets)
snegative =percentage(snegative, noOfTweets)
neutral =percentage(neutral, noOfTweets)
 # finding average reaction
polarity = polarity / noOfTweets

# printing out data
print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfTweets) + " tweets.")
print()
print("General Report: ")
if (polarity == 0):
   print("Neutral")
elif (polarity > 0 and polarity <= 0.3):
        print("Weakly Positive")
elif (polarity > 0.3 and polarity <= 0.6):
         print("Positive")
elif (polarity > 0.6 and polarity <= 1):
        print("Strongly Positive")
elif (polarity > -0.3 and polarity <= 0):
       print("Weakly Negative")
elif (polarity > -0.6 and polarity <= -0.3):
         print("Negative")
elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")
print()
print("Detailed Report: ")
print(str(positive) + "% people thought it was positive")
print(str(wpositive) + "% people thought it was weakly positive")
print(str(spositive) + "% people thought it was strongly positive")
print(str(negative) + "% people thought it was negative")
print(str(wnegative) + "% people thought it was weakly negative")
print(str(snegative) + "% people thought it was strongly negative")
print(str(neutral) + "% people thought it was neutral")

labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfTweets) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
