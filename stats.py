def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count_of_each_character = {}
    for character in text:
        character = character.lower()
        if character in count_of_each_character:
            count_of_each_character[character] += 1
        else:
            count_of_each_character[character] = 1

    count_of_each_character = sorted(count_of_each_character.items(), reverse=True, key=sort_dictionary)
    return count_of_each_character

def sort_dictionary(item):
    return item[1]