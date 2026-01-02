def count_words(text_content):
    words = text_content.split()
    
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_characters(text_content):

    character_dictionary = dict()
    
    for i in range(0, len(text_content)):
        lowercase_character = text_content[i].lower()
        
        if lowercase_character in character_dictionary:
            character_dictionary[lowercase_character] += 1
        else:
            character_dictionary[lowercase_character] = 1
        
    return character_dictionary

def sort_helper(items):
    return items["num"]

def sorted_list_dictionaries(dictionary):
    list_updated = []
    for i, y in dictionary.items():
        list_updated.append({"char":i, "num":y})
    
    list_updated.sort(reverse=True, key=sort_helper)

    return list_updated

