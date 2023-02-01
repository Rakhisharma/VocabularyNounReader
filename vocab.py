import json

from PyPDF2 import PdfReader

reader = PdfReader("a1_1.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

vocab = {}
genders = {"der": "m", "die": "f", "das": "n"}
for row in text.split("\n"):
    row = row.split(" ")
    if row[0] in ["der", "die", "das"] and row[1][0].isupper():
        vocab.update({row[1]: {"gender": genders[row[0]]}})

with open('vocab.json', 'w') as file:
    json.dump(vocab, file)
