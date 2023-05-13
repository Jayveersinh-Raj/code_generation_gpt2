from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer
from transformers.data import data_collator
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments
from tokenizer import tokenizer_main
from encode import encode

# tokenizer, and training files path
tokenizer, paths = tokenizer_main() 

# Assigning it to GPT2tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')

# Adding the special tokens
tokenizer.add_special_tokens({
    "eos_token": "</s>", 
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

config = GPT2Config(
    vocab_size = tokenizer.vocab_size,
    bos_token = tokenizer.bos_token_id,
    eos_token = tokenizer.eos_token_id
)

# Initialising model and dataset
model = GPT2LMHeadModel(config)
dataset = load_dataset("text", data_files = paths)

# Transformation
dataset.set_transform(encode)
dataset = dataset['train']

# Data collator from hugging face for LMs
data_collator = DataCollatorForLanguageModeling(tokenizer = tokenizer, mlm=True, mlm_probability = 0.15)

# Training arguments
training_args = TrainingArguments(
    output_dir = "code_generation",
    overwrite_output_dir = True,
    num_train_epochs = 1,
    per_device_train_batch_size = 32,
    save_steps = 100,
    save_total_limit = 2,
    prediction_loss_only = True
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset =dataset
)