import random
from hangmanWords import word_list
from hangmanArt import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f'you\'ve already guessed it')

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f'you guessed {guess}, that\'s wrong')
        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print(f"****************************IT WAS {chosen_word}! YOU WIN****************************")

    print(stages[lives])