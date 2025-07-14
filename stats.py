def num_words(book_text):
    words = book_text.split()
    return(len(words))

def character_count(book_text):
    lowercase = book_text.lower()
    characters = {}
    for character in lowercase:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters 

def make_list_from_dict(any_dict):
    result = [] # make an empty list
    for key, value in any_dict.items(): # for the dictionary, loop through the keys and add each key and each value to the key and value bins
        result.append({"key": key, "value": value})
    return result

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def sort_on(items):
    return items["value"]