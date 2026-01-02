from stats import count_words, count_characters, sorted_list_dictionaries
import sys

def main():
    text = ""
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    nr_of_words = count_words(text)
    dictionary_of_characters = count_characters(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {nr_of_words} total words")
    print("--------- Character Count -------")
    print_list(sorted_list_dictionaries(dictionary_of_characters))
    print("============= END ===============")

def print_list(sorted_dictionary):
    for i in range(len(sorted_dictionary)):
        if sorted_dictionary[i]["char"].isalpha() == True:
            print(f"{sorted_dictionary[i]["char"]}: {sorted_dictionary[i]["num"]}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()