import sys
from stats import get_num_words
from stats import get_num_characters_as_dict
from stats import get_sorted_num_characters_as_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        input_path = sys.argv[1]
        frankenstein_text = get_book_text(input_path)
        num_words_frankenstein = get_num_words(frankenstein_text)
        num_characters_frankenstein_dict = get_num_characters_as_dict(frankenstein_text)
        sorted_characters_list = get_sorted_num_characters_as_list(num_characters_frankenstein_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {input_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words_frankenstein} total words")
        print("--------- Character Count -------")
        for character in sorted_characters_list:
            character_value = character["char"]
            if character_value.isalpha():
                print(f"{character_value}: {character["num"]}")
        print("============= END ===============")
main()