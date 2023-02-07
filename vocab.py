import click
import json

from PyPDF2 import PdfReader


def read_pdf_to_json(file_path):
    reader = PdfReader(file_path)
    all_pages = len(reader.pages)
    vocab = []
    genders = {"der": "m", "die": "f", "das": "n"}
    for i in range(all_pages):
        page = reader.pages[i]
        text = page.extract_text()
        for row in text.split("\n"):
            row = row.split(" ")
            if row[0] in ["der", "die", "das"] and row[1][0].isupper():
                vocab.append({"name": row[1], "gender": genders[row[0]]})

    with open('vocab.json', 'w') as file:
        json.dump(vocab, file)

def main():
    read_pdf_to_json("a1_1.pdf")

if __name__ == '__main__':
    main()
