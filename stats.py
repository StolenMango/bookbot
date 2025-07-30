def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    words = file_contents.split()
    number_of_words = len(words)
    return number_of_words

def character_counter(file_contents):
    characters_dict = {
    }
    for char in file_contents:
        char = char.lower()
        if char in characters_dict:
            characters_dict[char] = characters_dict[char] + 1
        else: 
            characters_dict[char] = 1
    return characters_dict

def sort_on(characters_dict):
    list_of_dictionaries = []
    for key, value in characters_dict.items():
        list_of_dictionaries.append({"char": key, "num": value})
    list_of_dictionaries.sort(key=lambda item: item["num"], reverse=True)
    return list_of_dictionaries

def main():
    path = "books/frankenstein.txt"
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
