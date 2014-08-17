from __future__ import division
import sys
import json



tweet_list = []

def main():
	tweet()
	compute_frequency()


def tweet():
	tweet_file = open(sys.argv[1], 'r')
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


word_freq = {}

def compute_frequency():
	total = 0
	for item in tweet_list:
		words = item.split()
		for word in words:
			word.strip(" ")
			word = word.rstrip('?:!.,;"!@')
			word = word.lstrip('?:!.,;"!@')
			if word not in word_freq:
				word_freq[word] = 1
				total += 1
			else: 
				word_freq[word] += 1
				total += 1
	

	for word in word_freq:
		word_freq[word] /= total
		print word,float(word_freq[word])


if __name__ == '__main__':
    main()