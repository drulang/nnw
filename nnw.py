import sys
import os

mappings = {
    "a": [4, "@"],
    "b": ["13"],
    "c": ["("],
    "d": ["[)"],
    "e": [3],
    #"f": ["|="],
    "g": [6],
    #"h": ["|-|"],
    "i": [1, '!', "|"],
    #"j": [".]"],
    "k": ["|<"],
    "l": [1],
    "m": ['|Y|'],
    #"n": ["/\\/"],
    "o": [0],
    #"p": ["|>"],
    "q": ['0,'],
    #"r": ['|2'],
    "s": [5, "$"],
    "t": [7],
    "u": ['[_]','|_|'],
    "v": ['\\/'],
    "w": ['\\v/'],
    #"x": ['}{'],
    "y": ['`/'],
    "z": ['2'],
}

def parse_words(word_list):
    generated_words = []

    for word in word_list:
        parse_word(word, generated_words)

    return generated_words

def parse_word(word, generated_word_list):
    if word not in generated_word_list:
        generated_word_list.append(word)
    word_list = list(word) #Turn string into list so it's easier to do char replacement
    for letter in word:
        if letter.lower() in mappings:
            for alt_char in mappings[letter.lower()]:
                #Create a new word for each alt char
                char_index = word.index(letter)
                word_list[char_index] = str(alt_char)
                new_word = "".join(word_list)
                parse_word(new_word, generated_word_list)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Please pass in file location"
        exit(1)

    file_location = sys.argv[1]
    if not os.path.isfile(file_location):
        print "File does not exist or is a directory"
        exit(1)

    with open("nonowords", "w+") as bad_word_file:
        with open(file_location) as file_handle:
            for word in file_handle:
                if len(word) > 0:
                    bad_words = [] 
                    parse_word(word, bad_words) 
                    for bad_word in bad_words:
                        bad_word_file.write(bad_word)
