# Training a GPT-2 Model for Code Generation
This Python script trains a GPT-2 language model for code generation. It uses the Hugging Face's Transformers library for the GPT-2 model and tokenizer, and the Datasets library for handling the dataset.

# Steps:
- It starts by training a ByteLevelBPETokenizer on the provided text data file and saves the tokenizer model to disk. CUDA device order and visible devices are set according to your environment configuration.
- The trained tokenizer is then assigned to the GPT2Tokenizer and special tokens are added.
- A GPT-2 model is initialized with the GPT2Config class, using the vocab size and special tokens from the tokenizer.
- The dataset is loaded from the provided paths and transformed using the tokenizer.
- The data collator is set to DataCollatorForLanguageModeling from the Transformers library with masked language modeling enabled.
- Training arguments are set using the TrainingArguments class from Transformers, including output directory, number of epochs, batch size, save steps, etc.
- Finally, a Trainer is initialized with the model, training arguments, data collator, and dataset, and is ready to be trained.

# Note
This script uses PyTorch through the Transformers library. You need to have a compatible CUDA version installed if you wish to train the model on a GPU. 

# Check for nvidia
    
    nvidia-smi

My version:

+-------------------+ <br>
|CUDA Version: 12.0 | <br>
+-------------------+

# Example of input
<img width="212" alt="image" src="https://github.com/Jayveersinh-Raj/code_generation_gpt2/assets/69463767/93c19ce7-74b4-4639-8404-4077589c204a">

# Output of that for code suggestion/completion
<img width="181" alt="image" src="https://github.com/Jayveersinh-Raj/code_generation_gpt2/assets/69463767/afa54c8b-1fd3-4180-a343-6538958a57e7">

## Interpretations
The <N> signifies new line. On given import the model suggested the most viable imports it learned during training. 

## Key note
It is used as a proof of concept, and has been trained by checkpoints for multiple times, on multiple GPUs, and has been checked time to time before moving it on large scale. It is advised to do the same. The fine tuning on gpt2 itself is done to prototype with smaller models. But, as it can be seen that the results are very good, and improvement has been shown over time by the model during training. 

# Data and model
The dataset is provided, and scarpped by Advanced Engineering School (AES) of Innopolis University with whom the project is assosiated. Hence, data, and model/checkpoints are not open source. One can still scrap the data from github to prototype for learning purposes. The `data.py` file is provided as an example of how to do so. 