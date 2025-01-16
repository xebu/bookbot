def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_chars = get_character_count(text)
    new_list = get_only_alpha(count_chars)
    new_list.sort(reverse=True, key=sort_on)

    print_report(num_words, new_list)
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_only_alpha(dict):
    list_of_dicts = []
    for k in dict:
        datum = {}
        if k.isalpha() is True:
            datum["name"] = k
            datum["num"] = dict[k]
            list_of_dicts.append(datum)
    return list_of_dicts


def sort_on(dict):
    return dict["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(num_words, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for key in sorted_list:
        letter = key["name"]
        count = key["num"]
        print(f"The '{letter} character was found {count} times")

    print("--- End report ---")



main()
