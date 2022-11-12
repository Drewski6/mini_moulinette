import string  # Python module for strings. It contains a collection of string constants
import random  # Python's module for generating random objects
import os

# Generate letters

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase

# uppercase and lowercase word generators.


def uppercase_word():  # The function responsible for generating #random words which are in uppercase
    word = ''  # The variable which will hold the random word
    random_word_length = random.randint(1, 10)  # The random length of the word
    while len(word) != random_word_length:  # While loop
        word += random.choice(uppercase_letters)
    return word


def lowercase_word():  # The function responsible for generating #random words which are in uppercase
    word = ''  # The variable which will hold the random word
    random_word_length = random.randint(1, 10)  # The random length of the word
    while len(word) != random_word_length:  # While loop
        word += random.choice(lowercase_letters)
    return word

# Generate word list


word_list = []

# Generate wordlist 200 long. 100 upper case and 100 lower case.
for item in range(100):
    word_list.append(uppercase_word())
    word_list.append(lowercase_word())

# Save word list

with open("word_list.txt", "w") as file_wl:		# open file to save word_list.txt
    for item in word_list:
        file_wl.write(f"{item}\n")

# compile *_test.c Adjust path as needed. Make sure to link to your own library

os.system(f"gcc strrchr_test.c -L../libft/libft_working -lft")

# Header for csv file

header = "Function,Input String,Input Char,Return Value\n"

# Check functions

with open("word_list.txt", "r") as file_out:
    with open("output_OF.csv", "w") as OF:
        OF.write(header)
    with open("output_ft.csv", "w") as ft:
        ft.write(header)
    for item in word_list:
        # saves the output of the Original Function.
        os.system(f"./a.out 0 {item} >> output_OF.csv")
        # saves the output of the ft_function.
        os.system(f"./a.out 1 {item} >> output_ft.csv")

# Run diff.

if (os.system(f"diff output_OF.csv output_ft.csv") == 0):
    print("Congrats! No diff!")
