def get_num_words(text):
    return len(text.split())

def get_num_characters_as_dict(text):
    text = text.lower()
    dict = {}
    for character in text:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict

def num_characters_sort_on(dict):
    return dict["num"]

def get_sorted_num_characters_as_list(characters_dict):
    sorted_list = []
    for character in characters_dict:
        sorted_list.append({"char": character, "num": characters_dict[character]})
    sorted_list.sort(reverse=True, key=num_characters_sort_on)
    return sorted_list