# Tokenization Design of LLM Model which is based on Transformer.
from collections import Counter
import re

corpus = [
            "Hello world! This is my first tokenization function.",
            "Tokenization helps break text into smaller units.",
            "Transformers use vocabularies to map tokens to IDs."
         ]

def tokenization(text):

    text = "".join(text)

    sublist = []
    if text:
        text = text.lower()
        temp_list = re.findall(r"\w+|[^\w\s]",text)
        for token in temp_list:
            if re.match(r"\w+",token):
                sublist.extend(re.findall(r".{1,3}",token))
            else:
                sublist.append(token)
        return sublist
    else:
        return "text is emplty"

token_word = tokenization(corpus)

vocab = {"<PAD>": 0, "<UNK>": 1}

print(type(token_word))

for idx, token in enumerate(token_word,start=2):
    vocab[token]= idx

def text_to_id(my_test):

    token = tokenization(my_test)
    list_of_ids = [vocab[tok] for tok in token]
    return  list_of_ids

ids = text_to_id(["Hello world!"])

print(ids)




