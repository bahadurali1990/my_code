from datasets import load_dataset
from tokenizers import Tokenizer

from tokenizers.models import BPE

from tokenizers.trainers import BpeTrainer

from tokenizers.pre_tokenizers import Whitespace


# define classes

tokenizer = Tokenizer(BPE())

tokenizer.pre_tokenizer = Whitespace()

trainer  = BpeTrainer(vocab_size=5000,min_frequency=2,special_tokens=["<PAD>", "<UNK>", "<CLS>", "<SEP>"])

tokenizer.train([],trainer)


