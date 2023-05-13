from tokenizers import ByteLevelBPETokenizer
import os

def tokenizer_main() -> tuple[[ByteLevelBPETokenizer][os.path]]:
  """
  The function trains the tokenizer on a given text data file and saves the model to disk. 
  It also sets certain environmental variables for CUDA device order and visible devices.

  Parameters:
  -----------
  None

  Returns:
  -----------
  tokenizer: trained ByteLevelBPETokenizer
  path: path to the files for training
  """

  os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
  os.environ["CUDA_VISIBLE_DEVICES"] = "0, 1, 3, 4, 5"
  
  if not os.path.exists("tokenizer"):
      os.mkdir("tokenizer")
  
  TRAINABLE = True
  
  # Path to the file/files
  paths = [] # Assign your paths
  
  # Tokenizer
  if TRAINABLE:
    tokenizer = ByteLevelBPETokenizer()
    
    tokenizer.train(files=paths, vocab_size = 52_000, min_frequency = 2, special_tokens=[
        "<s>",
        "<pad>", 
        "</s>",
        "<unk>", 
        "<mask>",
    ])


    # Save files to disk
    tokenizer.save_model("tokenizer")
    return tokenizer