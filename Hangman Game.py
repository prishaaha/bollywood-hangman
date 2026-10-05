# hangman
from MOVIES import movies
import random

word = random.choice(movies)
#dictionary of key:()
hangman_art ={0: ("    ",
                  "    ",
                  "    "),
              1: ("   O  ",
                  "     ",
                  "     "),
              2: ("   O  ",
                  "   |  ",
                  "     "),
              3: ("   O  ",
                  "  /|  ",
                  "    "),
              4: ("   O  ",
                  "  /|\\  ",
                  "     "),
              5: ("   O  ",
                  "  /|\\  ",
                  "  /    "),
              6: ("   O ",
                  "  /|\\ ",
                  "  / \\"),
              7: ("|     ",
                  "|   O ",
                  "|  /|\\ ",
                  "|  / \\"),
              8: (" ____",
                  "|     ",
                  "|   O ",
                  "|  /|\\ ",
                  "|  / \\"),  
              9: (" ____",
                  "|   |  ",
                  "|   O ",
                  "|  /|\\ ",
                  "|  / \\"),     
            }


def display_hangman(wrong_guesses):
    
    for line in hangman_art[wrong_guesses]:
        print(line)
    

def display_hint(hint):
    print(" ".join(hint))

def display_ans(answer):
    print(" ".join(answer))

def main():
    print("Welcome to BOLLYWOOD Hangman!")
    answer = word 
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if "_"not in hint:
            display_hangman(wrong_guesses)
            display_ans(answer)
            print("YOU WIN!!")
            print("Congratulations! You've guessed the word!")
            is_running = False
        elif wrong_guesses >= 9:
            display_hangman(wrong_guesses)
            display_ans(answer)
            print("GAME OVER!!YOU LOSE!")
            print(f"You've run out of guesses. The word was '{answer}'.")
            is_running = False


if __name__ == "__main__":
    main()