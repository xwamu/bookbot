def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    char_count = count_chars(text)
    char_count_sorted = char_count_to_sorted_list(char_count)

    print(f"---= Report of {path} =---")
    print(f"{word_count} words found!")

    for item in char_count_sorted:
        if not item["char"].isalpha():
            continue 
        print(f"The '{item["char"]}' character has been found {item["num"]} times!")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def char_count_to_sorted_list(char_count_dict):
    sorted = []
    for char in char_count_dict:
        sorted.append({"char": char, "num": char_count_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

main()