Twitter-Sentiment-Analysis
==========================

Using the twitter API to stream tweets and perform basic sentiment analysis on them. The description of the files contained below:

- *twitterstream.py*: This file creates an authenticated connection with Twitter using the twitter API and then streams live tweets as they are recieved. This will be used to create the sample tweet file.  

- *tweet_sentiment.py*: Takes tweets and performs a basic sentiment analysis on the tweets to return a sentiment score for each tweet. This uses the AFINN-111.txt file which contains sentiment scores for a corpus of words. 

Sample command: python tweet_sentiment.py AFINN-111.txt sample.txt 

- *term_sentiment.py*: Calculates the sentiment scores for non-sentiment words/ words that do not have a score associated with it in AFINN-11.txt. Returns a list of words and their calculated sentiment scores.

python term_sentiment.py AFINN-111.txt sample.txt 

- *frequency.py*: This computes the term frequency histogram of the livestream data captured. This returns a given word and it's probability of appearing.

python frequency.py sample.txt 

- *Sample.txt*: Sample stream of tweets captured
- *AFINN-111.txt*: Word sentiment scores 
