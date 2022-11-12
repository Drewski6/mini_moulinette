*****************************************
# Mini Moulinette
*****************************************

- This python script and accompanying c program generates a random word list, and runs your ft function and the original function you specify against that word list.
- Here's how it works.

### How it works.

##### string_testing.py
1. Settings
	- This python dictionary makes configuring the script easier. Just put in the settings you want to configure.
	- C tester path
		- path to the custom tester you want to use. Just make sure your tester takes argv[1] as 0 or 1 for using original function or ft function. and argv[2] as input string.
	- libft path
		- path to your personal libft
	- word_list size
		- This is how many times you want to generate new words.
	- max word len
		- This indicates how long you want your generated words to be.
	- csv header
		- This is what values to print at the top of your csv files. Depends on what variables you want to print from your tester file.
		- I decided to save the output in csv so we can look at it as a table if we want. 
		- Set the header labels to whatever you like. 
		- Make sure they are consistant which the printf functions in the tester.
2. Generate letters.
	- Here we make 2 lists that contain all the ascii letters for capital and lower case.
	- You can add symbols if you want by making a list with all the symbols in it. I'm not doing that tho..
3. Uppercase and lowercase word generators
	- Here we define 2 functions that will make us words with length 1 to 10.
	- Again if you want to add symbols, just make another function that generates symbol words for you.
4. Generate word list
	- Here we use our functions to create 200 words. 100 are lower case and 100 are upper case.
	- We save all 200 elements in a list called word_list
5. Save word list
	- Just in case we want our word list for later, we save it to a file called word_list.txt
6. Compile
	- Here we compiler our tester. The tester is written in C and takes 2 arguments.
	- We will cover the tester in a bit. But for now here is an overview:
		- First argument is which function to run (ft or original)
		- Second argument is a string to run into the function.
7. Check Functions
	- Here we open our word list and read line by line each word.
	- We open both output_ft and output_OF and write our header into the file.
	- Then we iterate through the word list and run each word through our tester (a.out). Note that we indicate argv[1] as 0 for original function or 1 for 42 function.
	- We also append the output to the end of our output_ft and output_OF files.
8. Run diff
	- Finally run the diff command on both csv files to find any differences between your function and the original.


##### strrchr_test.c
- For this example, i am using a tester I made for the ft_strrchr.c
- Here we make a list of all the printable characters then loop over them and compare with the input string argv[2]
- the if statement in the while loop lets us choose which function we want to use (0 for original strrchr) (1 for ft_strrchr)
- the printf statement prints the same values as we saw in the header so everything is labeled nice. 
- printf prints to stdout which is redirrected with >> to output_ft.csv or output_OF.csv

### Final
- Feel free to use this however you like. This will only work for the ft_strrchr function IF you set it up correctly. You will need a new tester function if you want to use with any other functions. 
- The tester function is easy to make. Basically it takes an input argv[2] and decides which function to use with argv[1].
