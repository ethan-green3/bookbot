from stats import count_words
from stats import count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_of_each_character = count_characters(book_text)
    print(count_of_each_character)

main()