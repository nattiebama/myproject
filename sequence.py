# A code thats accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
my_string = "Welcome To Nattiebama Website" 
name_input = input("Enter your name here....",)
print("Welcome To Nattiebama!", name_input)

words = my_string.split()

# sort the list
words.sort()

# Display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
