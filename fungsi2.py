import string
from collections import Counter
from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer
import sys

def getNumberOfUppercaseWords(_list):
    n = 0
    for elem in _list:
        l = len(elem) #length of the token
        u = sum(c.isupper() for c in elem)      
        if u==l: #if all characters are in uppercase
            n+=1
    return n


try:
    stemmer = SnowballStemmer("english")
    file = open('test_fungsi2.py', 'r')
    sys.stdin= file
    exec( file )

    for line in file: 
        counter = Counter(line) #create a counter 
        number_of_character = len(line) 
        number_of_dollars = counter['$']           
        number_of_numeric = sum(c.isdigit() for c in line) #number of numeric value in the message
        line = line.translate(str.maketrans('.,;:/?!@#$&~#{([|-_^)]+=}*%', '                           '))
        tokens = line.split() #split the message into words
        number_of_uppercase_word = getNumberOfUppercaseWords(tokens)
        tokens = [stemmer.stem(token.lower()) for token in tokens]
        tokens.insert(0,number_of_character)
        tokens.insert(1,number_of_dollars)
        tokens.insert(2,number_of_numeric)
        tokens.insert(3,number_of_uppercase_word) 
        
        
except Exception as e:
    print('Error: ' + str(e))
