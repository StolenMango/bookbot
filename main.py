def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    words = file_contents.split()
    number_of_words = len(words)
    return number_of_words

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(contents)
    print(f"{word_count} words found in the document")

main()

