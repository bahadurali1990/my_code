import re
# Simples tokenization examples

"""text = "I am working on tokenization."

tokens = text.split(sep=None,maxsplit=-1)

print(tokens)"""

# problem with this tokenization.
# Problem 1: Punctuation Stays Attached

"""text = "I am working on tokenization. But what is the tokenizaiotn?"

tokens = text.split(sep=None,maxsplit=-1)

print(tokens)"""

# Solution of the above problem using regrex

"""text = "I am working on tokenization. But what is the tokenizaiotn?"

tokens = re.findall(r"\w+|[^\w\s]",text)

print(tokens)"""


"""text = "I am working on tokenization. But what is the tokenizaiotn? and I can't do this."

tokens = re.findall(r"\w+|[^\w\s]",text.lower())

print(tokens)"""









