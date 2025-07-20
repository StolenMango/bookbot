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

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    number_of_words = count_words(file_contents)
    characters = character_counter(file_contents)
    print(characters)
    print(f"{number_of_words} words found in the document")

main()
