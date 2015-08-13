import os
import nltk
from nltk.collocations import *
import string
from nltk.corpus import stopwords
import json
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# http://janda.org/politxts/Inaugural%20Addresses/table.htm

rootdir = '/Users/m_corneli/Documents/personal website/addresses/'
final = []
fd = {}
stop = stopwords.words('english')
# stop = ["the","of","and","to","in"]
for files, dirs, files in os.walk(rootdir):	
	for file in files:
		if str(file).endswith(".txt"):
			all = {}
			title = name = str(file)[:-4]
			all["name"] = title[:-5]
			all["year"] = title[-4:]
			print title
			f = open("addresses/" + str(file),"r")
			text=f.read()
			# collocations
			tokens = nltk.wordpunct_tokenize(text)
			tokens = [''.join(c for c in s if c not in string.punctuation) for s in tokens]
			tokens = [s for s in tokens if s]
			all["word_total"] = len(tokens)
			#BIGRAMS
			finder_b = BigramCollocationFinder.from_words(tokens)
			scored_b = finder_b.score_ngrams(bigram_measures.raw_freq)
			# sample = sorted(bigram for bigram, score in scored)
			all["bi_grams"] = sorted(finder_b.nbest(bigram_measures.raw_freq, 20))
			#TRIGRAMS
			finder_t = TrigramCollocationFinder.from_words(tokens)
			scored_t = finder_t.score_ngrams(trigram_measures.raw_freq)
			# sample = sorted(trigram for trigram, score in scored)
			all["tri_grams"] = sorted(finder_t.nbest(trigram_measures.raw_freq, 20))
			# creates dict 'fd' of terms and their frequencies in text
			for sent in nltk.sent_tokenize(text.lower()):
				for word in nltk.word_tokenize(sent):
					if word not in stop and word not in string.punctuation:
						try:
							fd[word] = fd[word]+1
						except KeyError:
							fd[word] = 1
			sort = sorted(fd, key=fd.__getitem__)
			top_words = {}
			for item in sort:
				 top_words[str(item)] = fd[item]
			all["top_words"] = top_words
			# for item in sort:
			# 	print item + ": " + str(fd[str(item)])
			fd = {}
			top_words = {}
			final.append(all)
			all = {}
# test = final[0]["top_words"]
# sort = sorted(test, key=test.__getitem__)
# for item in sort:
# 	print str(item) + ": " + str(test[item])
with open('addresses.json','w') as outfile:
	json.dump(final, outfile, indent=4)