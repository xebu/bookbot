def report(dict):
    
    my_list = sorted(list(dict.items()), key=lambda x: x[1], reverse=True)

    for item in my_list:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    



def count_letters(text):
    letter_counts = {}
    text = text.lower()
    
    for char in text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    
    return letter_counts

def letter_count(text):
    words = text.split()
    print(words)

def word_count(text):
    words = text.split()
    print(f"total numfer of words: {len(words)}")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()


print(file_contents)
word_count(file_contents)
letter_count(file_contents)
my_dict = count_letters(file_contents)
print(my_dict)
report(my_dict)