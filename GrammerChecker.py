#Grammer checker function
#Splitter function
#word checker with syllables
from autocorrect import spell
import difflib
#import enchant
import nltk
from nltk.corpus import wordnet
wordlist = open('E:/SpellChecker/wordlist.txt').read().splitlines()



def proper_word(word):
	if not wordnet.synsets(word):
		suggested1=suggestion(word)
		suggested=spell(word)
		return word,suggested1				#word suggestion
	else:
		return word



def suggestion(word):
	#print(word)
	result = difflib.get_close_matches(word, wordlist, n=5, cutoff=0.8)
	return result
	#print(result) # ['helot', 'hello', 'hel', 'helluo', 'helios']