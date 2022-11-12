import string  # Python module for strings. It contains a collection of string constants
import random  # Python's module for generating random objects
import os

# Settings for easy editing

settings = {"C tester path": "strrchr_test.c",
            "libft path": "../libft/libft_working",
            "word_list size": 100,
            "max word len": 10,
            "csv header": "Function,Input String,Input Char,Return Value\n",
            }

# Generate letters

# A constant containing lowercase letters
lowercase_letters = string.ascii_lowercase
# A constant containing uppercase letters
uppercase_letters = string.ascii_uppercase
# A constant containing digits
digits = string.digits
# All puntuation symbols (be careful using this. No escape characters)
symbols = string.punctuation
# All Whitespace characters
whitespace = string.whitespace
# A constant that contains whatever groups you like.
custom_word_symbols = lowercase_letters + uppercase_letters + digits + symbols

# uppercase and lowercase word generators.


def uppercase_word():  # The function responsible for generating #random words which are in uppercase
    word = ''  # The variable which will hold the random word
    random_word_length = random.randint(1, settings["max word len"])  # The random length of the word
    while len(word) != random_word_length:  # While loop
        word += random.choice(uppercase_letters)
    return word


def lowercase_word():  # The function responsible for generating #random words which are in uppercase
    word = ''  # The variable which will hold the random word
    random_word_length = random.randint(1, settings["max word len"])  # The random length of the word
    while len(word) != random_word_length:  # While loop
        word += random.choice(lowercase_letters)
    return word


def custom_word():  # This function generates a word with any mix of characters you like.
    word = ''  # The variable which will hold the random word
    random_word_length = random.randint(1, settings["max word len"])  # The random length of the word
    while len(word) != random_word_length:  # While loop
        word += random.choice(custom_word_symbols)
    return word

# Generate word list


word_list = []

# Generate wordlist 200 long. 100 upper case and 100 lower case.

for item in range(int(settings["word_list size"])):
    word_list.append(uppercase_word())
#	word_list.append(custom_word())				# get ready for syntax errors if you use this! lol
    word_list.append(lowercase_word())

# Save word list

with open("word_list.txt", "w") as file_wl:		# open file to save word_list.txt
    for item in word_list:
        file_wl.write(f"{item}\n")

# Compile *_test.c Adjust path as needed. Make sure to link to your own library.

os.system(f"gcc {settings['C tester path']} -L{settings['libft path']} -lft")

# Check functions

# runs word_list through both the original function (a.out 0) and 42 function (a.out 1)
with open("word_list.txt", "r") as file_out:
    with open("output_OF.csv", "w") as OF:
        OF.write(settings["csv header"])
    with open("output_ft.csv", "w") as ft:
        ft.write(settings["csv header"])
    for item in word_list:
        # saves the output of the Original Function.
        os.system(f"./a.out 0 {item} >> output_OF.csv")
        # saves the output of the ft_function.
        os.system(f"./a.out 1 {item} >> output_ft.csv")

# Run diff.

if (os.system(f"diff output_OF.csv output_ft.csv") == 0):
    print("Congrats! No diff!")
