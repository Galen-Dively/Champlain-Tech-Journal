# Galen Dively
# CSI-260
# List Comprehension Lab


# Generate a list of all of the numbers from 1-1000 that are divisible by 7
def nums_divisble_by_seven():
    return [i for i in range(1, 1000) if i % 7 == 0]

# Generate a list of all of the numbers from 1-1000 that have the digit 3 in them
def has_three():
    return [i for i in range(1, 1000) if str(3) in str(i)]


# Remove all of the vowels in a string (can assume y is not a vowel)
def remove_vowels(string):
    vowels = ["a", "e", "i", "u", "o"] # list of vowels to use
    filterd =  [i for i in string if i not in vowels] # create the list of constants 
    new_string = "" # start return string
    for i in filterd:
        new_string += i # add the filtered character to the string
    return new_string

# Find all of the words in a string that are less than 4 letters
def less_than_four(string: str):
    return [word for word in string.split() if len(word) < 4]


# Use a dictionary comprehension that maps each each word in a sentence to its length.
def map_word_to_length(string):
    wordlist = string.split() # list of words
    lengths = [len(word) for word in wordlist] # list of lengths of words in wordlist
    assert(len(wordlist) == len(lengths)) # make sure they are they same
    return {wordlist[i] : lengths[i] for i in range(len(wordlist))} # creates a dictionary with the word as the key and the length as the value


#Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
def divisible_by_single_digit():
    return list(set([i for i in range(1, 1000) for j in range(2, 9) if i % j == 0])) # use set to remove duplicates


# example string 
example_string  = "The quick brown fox jumped over the lazy dog"


def main():
    # Main function that prints the other functions
    print(f"1. Numbers Divisible by Seven\n{nums_divisble_by_seven()}")
    input("Press Enter to Continue")
    print(f"2. Numbers that contain a 3\n{has_three()}")
    input("Press Enter to Continue")
    print(f"3. Remove vowels from a sentence\n{remove_vowels(example_string)}")
    input("Press Enter to Continue")
    print(f"4. Words with Less then four characters\n{less_than_four(example_string)}")
    input("Press Enter to Continue")
    print(f"5. Dictionary of words mapped to respective length \n {map_word_to_length(example_string)}")
    input("Press Enter to Continue")
    print(f"6. Numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)\n{divisible_by_single_digit()}")

main()
