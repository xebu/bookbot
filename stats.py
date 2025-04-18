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


def sort_on(dict):
    return dict["num"]


def get_only_alpha(dict):
    list_of_dicts = []
    for k in dict:
        datum = {}
        if k.isalpha() is True:
            datum["name"] = k
            datum["num"] = dict[k]
            list_of_dicts.append(datum)
    return list_of_dicts
