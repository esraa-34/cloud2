my_file1=open("book1e.txt",'rt')
text1 = my_file1.read()
my_file1.close()
word1 = text1.split()

import string
table1 = str.maketrans('', '', string.punctuation)
text1 = [w.translate(table1) for w in word1]

text1 = [word.lower() for word in text1]


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words1 = set(stopwords.words('english'))
text1 = [w for w in text1 if not w in stop_words1]


my_file2=open("book2e.txt",'rt')
text2 = my_file2.read()
my_file2.close()
word2 = text2.split()

import string
table2 = str.maketrans('', '', string.punctuation)
text2 = [w.translate(table2) for w in word2]

text2 = [word.lower() for word in text2]

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words2 = set(stopwords.words('english'))
text2 = [w for w in text2 if not w in stop_words2]

c=0

for x in set(text1):
 for y in set(text2):
    if x==y and  x!='' and y!='' :
        print (x)
        c=c+1
        
print(c)