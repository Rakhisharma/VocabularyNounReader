import click
import json

from PyPDF2 import PdfReader


def read_pdf_to_json(file_path):
    reader = PdfReader(file_path)
    all_pages = len(reader.pages)
    vocab = []
    genders = {"der": "m", "die": "f", "das": "n"}
    index = 0
    for i in range(all_pages):
        page = reader.pages[i]
        text = page.extract_text()
        for row in text.split("\n"):
            row = row.split(" ")
            if row[0] in ["der", "die", "das"] and row[1][0].isupper():
                vocab.append({"id": index, "name": row[1], "gender": genders[row[0]]})
                index += 1
    file_name = file_path.replace('.pdf', '') + '.json'
    with open(file_name, 'w') as file:
        json.dump(vocab, file)

@click.command()
@click.option('-f', '--file', help='Path to PDF.')
def main(file):
    read_pdf_to_json(file)

if __name__ == '__main__':
    main()
