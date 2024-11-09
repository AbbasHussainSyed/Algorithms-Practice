# Define a string named 'word' to represent the phrase we'll work with
word = 'FRUIT Salad'

# Initialize a counter to hold the number of non-vowel characters
counter = 0

# Use a 'for' loop to iterate over each character in the string
for i in word.strip():
    # Convert character to lowercase and check if it is not a vowel or a space
    if i.lower() not in "aeiou ":
        counter += 1

# Finally, print out the count of non-vowel characters
print(counter)