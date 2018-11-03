

import nltk
line = 'how to implement quicksort in python'
tokens = nltk.word_tokenize(line)
pos_tags = nltk.pos_tag(tokens)
for word,pos in pos_tags:
     if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             print (word)


# from textblob import  TextBlob
# blob = TextBlob("""Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
# actions between computers and human (natural) languages""")
# print(blob.noun_phrases)