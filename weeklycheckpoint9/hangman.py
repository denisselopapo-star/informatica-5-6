#import random
import random
# Define the main function
def main():
# Create the txt file for the words
# add the words to the file
# define the function called start_game(file)

    start_game("words.txt")
def start_game(file):

    with open(file) as new_file:
        content = new_file.read().splitlines()
    words = random.choice(content)
    count = len(words)

    slash = ["_"]* count
    print(" ".join(slash))

    while True:
        guess = input("Take a guess: ").strip()
        if len(guess) == 1:
            break
        else:
                print("Invalid guess. Try again.")
    for i in secret_word:
        



if __name__=="__main__":
    main()
