import nltk

from nltk import word_tokenize
from nltk import sent_tokenize

nltk.download('punkt_tab')

my_sentence = "India is a greate country. And Delhi is the Capital of India"

sen_tokens  = sent_tokenize(my_sentence)
work_token  = word_tokenize(my_sentence)

print(sen_tokens)
print(work_token)

