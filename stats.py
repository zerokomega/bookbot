def get_book_text(file_path):
    file_contents = file_path.read()
    return file_contents

def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_character_count(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    
    return character_count

def sort_on(dict):
    return dict["count"]

def split_to_sorted_list(dict):
    sorted_list = []
    for key, value in dict.items():
        sorted_list.append({"character": key, "count": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
