from transformers import AutoTokenizer, AutoModelForCausalLM
# from flask import Flask, request, jsonify
# app = Flask(__name__)
import os

folder = 'doc_func' # doc_only / func_only / doc_func
path = f"/Users/cindy/code-generation/{folder}/input"
os.chdir(path)

device = "cpu"  # "cpu" or "cuda" or "cuda:n" where n is specific GPU to use
modelname = "EleutherAI/gpt-neo-2.7B"
tokenizer = AutoTokenizer.from_pretrained(modelname)
model = AutoModelForCausalLM.from_pretrained(modelname)
model.to(device)

# with open('text.txt', 'r') as file:
#     prime = file.read()

def inference(prompt, temperature, max_length):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    input_ids = input_ids.to(device)
    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=temperature,
        max_length=max_length,
    )
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    return gen_text


def autocomplete(plaintext, to_prime=True, temperature=0.8, max_length=300):
    # prompt = prime + plaintext if to_prime else plaintext
    prompt = plaintext
    generation = inference(prompt, temperature, max_length)
    return generation[len(prompt) :].split("###")[0]

# @app.route("/")
def arguments(text, file_name):
    # text = "Convert list of strings into ints and return its sum" # read from file
    generation = autocomplete(text)
    f = open(f"/Users/cindy/code-generation/{folder}/output/"+file_name.rsplit('.', 1)[0]+"-output.txt", "w")
    f.write(generation)
    f.close()

try:
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            with open(file_path, 'r') as f:
                arguments(f.read(), file)
            print(file_path + " ran successfully")
        else:
            print(f"No text files in {path}")
except FileNotFoundError:
    print('File not found')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="9900")