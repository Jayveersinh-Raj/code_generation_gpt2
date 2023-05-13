from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("tokenizer") # your tokenizer path
model = AutoModelWithLMHead.from_pretrained("code_generation") # your model path

# copy and paste some code in here
print("Enter the code for completion")
inp = input(">>>")

newlinechar = "<N>"
converted = inp.replace("\n", newlinechar)
tokenized = tokenizer.encode(converted, return_tensors='pt')
resp = model.generate(tokenized)

decoded = tokenizer.decode(resp[0])
reformatted = decoded.replace("<N>","\n")

print(reformatted)
