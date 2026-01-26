from collections import Counter,deque
from functools import lru_cache
import json

class BPETokenizerSimple:

    def __init__(self):

        self.vocab = {}

        self.inverse_vocab = {}

        self.bpe_merges = {}

        self.bpe_ranks = {}

    def train(self,text,vocab_size,allowed_special={"<|endoftext|>"}):
        """
               Train the BPE tokenizer from scratch.

               Args:
                   text (str): The training text.
                   vocab_size (int): The desired vocabulary size.
                   allowed_special (set): A set of special tokens to include.
        """

        # Preprocess: Replace spaces with "Ġ"
        # Note that Ġ is a particularity of the GPT-2 BPE implementation
        # E.g., "Hello world" might be tokenized as ["Hello", "Ġworld"]
        # (GPT-4 BPE would tokenize it as ["Hello", " world"])

        processed_text = []

        for i , char in enumerate(text):
            if char==" " and i!=0:
                processed_text.append("G")
            if char!=" ":
                processed_text.append(char)

        processed_text = "".join(processed_text)

        unique_char = [chr(i) for i in range(256)]

        unique_char.extend(char for char in sorted(set(processed_text)) if char not in unique_char)

        if "Ġ" not in unique_char:
            unique_char.append("Ġ")

        self.vocab = {i:char for i, char in enumerate(unique_char)}

        self.inverse_vocab = {char : i for char ,i in self.vocab.items()}

        if allowed_special:

            for token in allowed_special:
                if token not in self.inverse_vocab:
                    new_id = len(self.vocab)
                    self.vocab[new_id]=token
                    self.inverse_vocab[token]=new_id

        token_ids = [self.inverse_vocab[char] for char in processed_text]

        for new_id in range(len(self.vocab), vocab_size):
            






