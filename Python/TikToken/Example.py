# Example.py

import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

def tokenize(text):
    tokens = encoding.encode(text)
    return tokens

def count_tokens(tokens):
    return len(tokens)

def decode_tokens(tokens):
    return encoding.decode(tokens)