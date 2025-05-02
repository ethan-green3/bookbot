import sys

from stats import count_words
from stats import count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    len_args = len(sys.argv)
    if len_args != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1] 

    if book_file == "":
        print("Please provide a book file to analyze")
        sys.exit(1)
    print(book_file)
    book_text = get_book_text(book_file)
    word_count = count_words(book_text)
    count_of_each_character = count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count -------")
    for character, count in count_of_each_character:
        if not character.isalpha():
            continue
        print(f"{character}: {count}")
    print("============= END ===============")

main()