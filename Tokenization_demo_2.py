# Implementation of tokenization with Punctuation
import re

text = "I am going to implement Tokenization in python from scratch."

tokens = re.findall(r"\w+|[^\s\w]", text)

print(tokens)
