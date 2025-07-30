from stats import get_book_text
from stats import count_words
from stats import character_counter
from stats import sort_on
import sys

def main():
    # path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_book_text(path)
    number_of_words = count_words(file_contents)
    characters_dict = character_counter(file_contents)
    sorted_list = sort_on(characters_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    # print(characters_dict)
    # print(sorted_list)

main()