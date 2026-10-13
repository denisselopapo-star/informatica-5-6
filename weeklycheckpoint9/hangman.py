#import random
import random
# Define the main function
def main():
# Create the txt file for the words
# add the words to the file
# define the function called start_game(file)

    start_game(file)
    def start_game(file):

        with open("words.txt") as new_file:
            content = new_file.read().splitlines()
            print(random.choice(content))



