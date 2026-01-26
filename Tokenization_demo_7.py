import re
import wikipedia

def tokenization(text: str) -> list:
    """
    Tokenize the input text into words and punctuation,
    then append special tokens used in NLP tasks.

    Args:
        text (str): Input text string.

    Returns:
        list: List of tokens including special tokens.
    """
    # Define special tokens commonly used in NLP models
    special_tokens = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]

    # Convert text to lowercase for consistency
    text = text.lower()

    # Split text into words and punctuation using regex
    tokens = re.findall(r"\w+|[^\w\s]", text)

    # Append special tokens to the token list
    tokens = tokens + special_tokens

    return tokens


def create_vocab() -> dict:
    """
    Create a vocabulary dictionary from the content of the
    Wikipedia page 'India (country)'.

    Each unique token is assigned a unique integer ID.

    Returns:
        dict: Vocabulary mapping token -> integer ID.
    """
    # Fetch Wikipedia page content and split into lines
    page_content = wikipedia.page("India (country)").content.splitlines()

    # Join lines into a single string
    text = "".join(page_content)

    vocab = {}

    # Tokenize the text
    tokens = tokenization(text)

    # Convert tokens to a set to keep only unique values
    tokens = set(tokens)

    # Assign each token a unique index
    for idx, word in enumerate(tokens):
        vocab[word] = idx

    return vocab


def encode(test: str, vocab: dict) -> list:
    """
    Encode a given text string into a list of token IDs
    based on the provided vocabulary.

    Args:
        test (str): Input text string to encode.
        vocab (dict): Vocabulary mapping token -> integer ID.

    Returns:
        list: List of integer IDs representing the tokens.
    """
    # Tokenize the input text
    tokens = tokenization(test)

    ids = []

    # Convert each token into its corresponding ID
    for token in tokens:
        ids.append(vocab[token])  # Assumes token exists in vocab

    return ids


def decode(input: list, vocab: dict) -> str:
    """
    Decode a list of token IDs back into a string using the vocabulary.

    Args:
        input (list): List of integer IDs to decode.
        vocab (dict): Vocabulary mapping token -> integer ID.

    Returns:
        str: Decoded string reconstructed from token IDs.
    """
    temp_str = []

    # Create reverse dictionary (id -> token)
    reverse_vocab = {value: key for key, value in vocab.items()}

    # Convert each ID back into its token
    for id in input:
        temp_str.append(reverse_vocab[id])

    # Join tokens into a single string
    my_str = " ".join(temp_str)

    return my_str


# Build vocabulary from Wikipedia page
vocab = create_vocab()

# Example text to encode
text = "the British Indian Empire  was partitioned into two independent dominions"

# Encode text into token IDs
my_ids_tokens = encode(text, vocab)

# Decode IDs back into text
my_original_text = decode(my_ids_tokens, vocab)

# Print results
print(f"My Original text is ::: {text}")

print(f"My Token after encode function ::: {my_ids_tokens}")

print(f"My Original text after decode functions ::: {my_original_text}")
