def main():
    path_for_book = "books/frankenstein.txt"
    clear_text = get_book_text(path_for_book)
    # print(clear_text)
    word_count(clear_text)
    character_count(clear_text)

# split() clear text and count with len()
def word_count(text):
    words = text.split()
    print(len(words))

# 
def character_count(text):
    char_count = {}
    words = text.lower().split()
    # print(words)
    for word in words:
        chars = list(word)
        # print(chars)
        for char in chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    print(char_count)


def get_book_text(path_for_book):
    with open(path_for_book, "r") as f:
        return f.read()

main()