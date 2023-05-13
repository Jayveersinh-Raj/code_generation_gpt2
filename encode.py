from tokenizer import tokenizer_main

# tokenizer, and training files path
tokenizer, paths = tokenizer_main() 

def encode(lines: str) -> tokenizer.encode:
  """
  A function to encode texts using tokenizer

  Parameters:
  -----------
  lines: text to be encoded

  Returns:
  ----------
  Encoded text using tokenizer
  """
  
  return tokenizer(lines['text'], add_special_tokens=True, truncation=True, max_length = 1024)