import sys 
from stats import get_book_text
from stats import num_words
from stats import character_count
from stats import make_list_from_dict
from stats import sort_on


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    count = num_words(book_text)
    characters = character_count(book_text)
    chars_list = make_list_from_dict(characters)
    chars_list.sort(reverse=True, key=sort_on)
    # If False, do nothing (skip)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in chars_list:
        char = item["key"]     # This is a string, like "a" or "1" or "!"
        if char.isalpha():      # Only True for letters
            print(f"{char}: {item['value']}")

    print("============= END ===============")

main()

