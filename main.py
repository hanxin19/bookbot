def main():
    path_for_book = "books/frankenstein.txt"
    clear_text = get_book_text(path_for_book)
    # print(clear_text)
    # word_count(clear_text)
    # print(character_count(clear_text))
    print_report(path_for_book, clear_text)

# prints out a worded report of word- and character counts
def print_report(book_title, text):
    print(f"--- Begin report of {book_title} ---\n")
    print(f"{word_count(text)} words found in the document.")
    counted_chars = character_count(text)
    for character, quantitiy in counted_chars.items():
        print(f"The {character} character was found {quantitiy} times.")
    print("--- End report ---")

# split() clear text and return words counted with len()
def word_count(text):
    words = text.split()
    return len(words)

# counts all characters and stores in dict {str : int}
def character_count(text):
    char_count = {}
    words = text.lower().split()
    # print(words)
    for word in words:
        chars = list(word)
        # print(chars)
        for char in chars:
            if char.isalpha() == True:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count


def get_book_text(path_for_book):
    with open(path_for_book, "r") as f:
        return f.read()

main()