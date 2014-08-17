import sys
import json


scores = {}
tweet_list = []
score_list = []



def lines(fp):
    print str(len(fp.readlines()))

def main():
    sentiment()
    tweet()
    map_sentiment()



def sentiment():
	affinfile = open(sys.argv[1], 'r')
	for line in affinfile:
		term, score = line.split("\t")
		scores[term] = int(score)

def tweet():
	tweet_file = open(sys.argv[2], 'r')
	key = 'text'
	lang = 'en'
	for line in tweet_file:
		result = (json.loads(line))
		if key in result and result['lang'] == lang:
			try:
				t = result['text'].encode('utf-8')
				tweet_list.append(t)
			except:
				print "something went wrong"


def map_sentiment():
	for item in tweet_list:
		sum = 0
		words = item.split()
		for word in words:
			if word in scores.keys():
				sum += scores[word]
			
			else:
				sum += 0
			
		score_list.append(sum)

	for score in score_list:
		print score
   		



if __name__ == '__main__':
    main()
