import sys

from stats import get_book_text
from stats import get_num_words
from stats import get_character_count
from stats import split_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as f:
        book_text = get_book_text(f)
        num_words = get_num_words(book_text)
        character_count = get_character_count(book_text)
        sorted_list = split_to_sorted_list(character_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in sorted_list:
            if dict["character"].isalpha() is True:
                print(f"{dict["character"]}: {dict["count"]}")
        print("============= END ===============")

main()