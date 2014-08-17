import sys
import json


scores = {}
tweet_list = []


def main():
    sentiment()
    tweet()
    compute_sentiment()

  

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
		if key in result:
			try:
				t = result['text'].encode('utf-8')
				tweet_list.append(t)
			except:
				print "something went wrong"

derived_score = {}
freq_count = {}

def compute_sentiment():
	for item in tweet_list:
		sum = 0
		print item
		words = item.split()
		for word in words:
			word.strip(" ")
			word = word.rstrip('?:!.,;"!@')
			word = word.lstrip('?:!.,;"!@')
			word.lower()
			if word in scores:
				sum += scores[word]		
			else:
				sum += 0
				na_words.append(word)

		for word in na_words:
			if word not in derived_score: 
				derived_score[word] = sum
				freq_count[word] = 1
			else:
				derived_score[word] += sum
				freq_count[word] += 1


	for term in derived_score:
		derived_score[term] /= freq_count[term]
		print term + " " + str(derived_score[term])
   		



if __name__ == '__main__':
    main()