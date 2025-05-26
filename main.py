from stats import num_of_words_in_text, chars_frequency, sorted_list
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_of_words = num_of_words_in_text(text)
    frequency_of_chars = chars_frequency(text)
    list_of_chars = sorted_list(frequency_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for value in list_of_chars:
        if value["char"].isalpha():
            print(f"{value["char"]}: {value["num"]}")
    print("============= END ===============")
    
main()