import nltk
from nltk.tokenize import RegexpTokenizer 
from nltk.corpus import stopwords

'''
s = 'At eight oclock on Thursday morning... Arthur didn	t feel very good.'

tokens = nltk.word_tokenize(s)
print(tokens)
'''

f = open("text.txt","r")
#s = nltk.word_tokenize(f.read())

tokenizer = RegexpTokenizer('\w+')
s = tokenizer.tokenize(f.read())

freq = nltk.FreqDist(x.lower() for x in s)
#freq = dict(freq)

#print(freq.most_common(100))
#print(freq)

print('--------------------\n\n')
#print(stopwords.words('english'))

#dictionary

from PyDictionary import PyDictionary

dictionary=PyDictionary("hotel","cricket")
#There can be any number of words in the Instance

#print(dictionary.printMeanings()) #This print the meanings of all the words
print(dictionary.getMeanings())   #This will return meanings as dictionaries
#print(dictionary.getSynonyms())

