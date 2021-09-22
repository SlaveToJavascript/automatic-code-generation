# https://huggingface.co/EleutherAI/gpt-neo-2.7B
from transformers import pipeline
# from flask import Flask
# app = Flask(__name__)

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

with open('existing.py', 'r') as file:
    prime = file.read()
prime = "'''\n" + prime + "\n''''"
# print(prime)

# @app.route("/")
# def foo():
with open('text.txt', 'r') as file:
    text = file.read()
gen_text = generator(prime+text, do_sample=True, min_length=50)
# Output = [{'generated_text': '...'}]
print(gen_text[0]['generated_text'])

# if __name__ == '__main__':
#     app.run(host="localhost", port=8000, debug=True)