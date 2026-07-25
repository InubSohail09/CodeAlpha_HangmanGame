import random

# list of words the game can pick from
word_list = ["python", "hangman", "computer", "keyboard", "program", "Apple", "Congratulations"]

def choose_word():
    return random.choice(word_list)

def play_game():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 5

    print("Heyyyy Inub!!! Welcome to Hangman!")
    print("Try to guess the word.Can you..? You have", max_wrong, "wrong guesses allowed.\n")

    while wrong_guesses < max_wrong:
        # build the display word, showing _ for letters not guessed yet
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word: ", display_word)
        print("Wrong guesses left:", max_wrong - wrong_guesses)

        # check if player has already won
        if display_word == word:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        # basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    # if loop ended because wrong_guesses reached the max
    if wrong_guesses == max_wrong:
        print("You lost! The word was:", word)

def main():
    play_again = "yes"
    while play_again == "yes":
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

    print("ThankYouu for playing! See you Again")

main()