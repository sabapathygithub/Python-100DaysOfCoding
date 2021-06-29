# Step 1
import random
import hangman_words
import  hangman_art

stages = hangman_art.stages

word_list = ["apple", "ball", "camel", "doll", "elephant"]

lifes = 6

chosen_word = random.choice(hangman_words.word_list)


display = ["_"] * len(chosen_word)

# print(f"{' '.join(display)}")

end_of_game = False
print(hangman_art.logo)
print(f"The word is {chosen_word}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for index, char in enumerate(chosen_word):
        if char == guess:
            display[index] = guess
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lifes -= 1
        print(stages[lifes])

    if lifes == 0:
        end_of_game = True
        print("You lose. Game is over")
    elif "_" not in display:
        end_of_game = True
        print("You win")