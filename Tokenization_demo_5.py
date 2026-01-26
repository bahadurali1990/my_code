# implement lower cases in your tokenization processs
import re
import wikipedia

def tokenization(text:str)-> list:

    special_tokens = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]

    text = text.lower()

    tokens = re.findall(r"\w+|[^\w\s]", text)

    tokens = tokens + special_tokens

    return tokens

page_content = wikipedia.page("India (country)").content.splitlines()

text = "".join(page_content)

tokens = tokenization(text)

print(tokens)



