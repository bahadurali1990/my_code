# Simple tokenizers with Special tokens and Punctuation

import re

special_tokens = ["[PAD]","[UNK]","[CLS]","[SEP]","[MASK]"]

text = "I am going to implement Tokenization in python from scratch."

tokens = re.findall(r"\w+|[^\w\s]",text)

tokens = tokens+special_tokens

print(tokens[:10])


