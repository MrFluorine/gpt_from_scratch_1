import re
import tiktoken
## Step 1: creating tokens from data
with open("the-verdict.txt", "r", encoding= "utf-8") as f:
    raw_text = f.read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [word.strip() for word in preprocessed if word.strip()]
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
## Step 2: creating vocabulary from data
vocab_size = len(all_tokens)
vocab = {token:integer for integer, token in enumerate(all_tokens)}

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:v for v,i in vocab.items()}
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [word.strip() for word in preprocessed if word.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
# tokenizer = SimpleTokenizerV1(vocab)
text = """ Hello, do you like tea? <|endoftext|> In the sunlit terraces of palace
"""

# ## Step 3: Encode the text using the BPE tokenizer
# tokenizer = tiktoken.get_encoding("gpt2")
# ids = tokenizer.encode( text, allowed_special = {"<|endoftext|>"})
# print(tokenizer.decode(ids))