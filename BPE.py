from datasets import load_dataset
from tokenizers import Tokenizer

from tokenizers.models import BPE

from tokenizers.trainers import BpeTrainer

from tokenizers.pre_tokenizers import Whitespace


# define classes

tokenizer = Tokenizer(BPE())

tokenizer.pre_tokenizer = Whitespace()

trainer  = BpeTrainer(vocab_size=5000,min_frequency=2,special_tokens=["<PAD>", "<UNK>", "<CLS>", "<SEP>"])

from pdfminer.high_level import (extract_text)
pdf_path = "/Users/ahad/India - Wikipedia.pdf"
text = extract_text(pdf_path) # Save to a .txt file
with open("india_wikipedia.txt", "w", encoding="utf-8") as f: f.write(text)

tokenizer.train(["india_wikipedia.txt"],trainer)

tokenizer.save("wiki-tokenizer.json")

tokenizer = Tokenizer.from_file("wiki-tokenizer.json")
output = tokenizer.encode("Tokenization is powerful!")
print(output.tokens)


