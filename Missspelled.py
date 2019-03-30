import re
import GrammerChecker
 # Spelling correcter
#sample="wellcom."
regex=r"^([A-Za-z]+)([^ A-Za-z\n]+|[A-Z]+)([A-Za-z.?!]+|(?<![.?!]))$"
newRex=r"([A-Za-z]+([\-\_\.\$\*\+\,\/\\\)\(\[\]\{\}0-9])[A-Za-z]+)"
#splitr=r"[\-\_\.\$\*\+\,\/\\\)\(\[\]\{\}0-9]"



regex=re.compile(regex)

def regexTester(word):
	wordlist=[]
	firstWord=""
	secondWord=""
	breaker=""
	finds=re.search(regex,word)
	if finds:
		if finds.group(1):
			firstWord=finds.group(1)
			#print("first=",finds.group(1))
		if finds.group(3):
			secondWord=finds.group(3)
			#print("second=",finds.group(3))
		if finds.group(2).isalpha():
			breaker=finds.group(2)
			#print("matched=",finds.group(2))



		#first,second=re.split(splitr,finds[0])
		#print(firstWord,secondWord)
		for word in [firstWord,secondWord]:
			if len(word)>0:
				wordlist.append(GrammerChecker.proper_word(word))
		return wordlist
	else:
		return(GrammerChecker.proper_word(word))


# print(regexTester("alrigh-righ"))