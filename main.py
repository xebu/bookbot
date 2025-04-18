import sys
from stats import get_num_words, get_character_count, sort_on, get_only_alpha


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(num_words, sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for key in sorted_list:
        letter = key["name"]
        count = key["num"]
        print(f"{letter}: {count}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_chars = get_character_count(text)

    new_list = get_only_alpha(count_chars)
    new_list.sort(reverse=True, key=sort_on)

    print_report(num_words, new_list)


main()
