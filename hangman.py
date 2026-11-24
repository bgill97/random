import string

print('Welcome to hangman!')
full_alphabet = list(string.ascii_lowercase)
print(f"Full alphabet: {full_alphabet}")

already_guessed = []
available_letters = full_alphabet


def replace_with_asterisk(text):
    return '*' * len(text)


while True:
    choice = input('Please enter a word: ')
    if choice.isalpha() is False:
        print('That is not a word.')
        continue
    if len(choice) > 10:
        print('That word is too long.')
        continue
    else:
        print(f"The word you chose is {choice}.")
        break

masked_word = replace_with_asterisk(choice)
guesses_remaining = 5

while True:
    print(f"Guesses remaining: {guesses_remaining}")
    if masked_word == choice:
        print(f"You won! The word is {choice}.")
        print('Game over.')
        break
    elif guesses_remaining == 0:
        print(f"You have {guesses_remaining} guesses remaining. The game is over.")
        break
    elif guesses_remaining < 5:
        guess_word_user_response = input(f"So far you have {masked_word}.\nWould you like to guess the word? (Y/N)")
        if guess_word_user_response.upper() == 'Y':
            guess = input('Guess: ')
            if guess == choice:
                print(f"You won! The word is {choice}.")
                print('Game over.')
            else:
                print('That is not the word.')
                guesses_remaining -= 1
        elif guess_word_user_response.upper() == 'N':
            pass
        else:
            print('That is not a valid response.')
            continue
    else:
        pass
    print(f"Already guessed: {already_guessed}")
    print(f"Available letters: {available_letters}")
    print(f"Progress: {masked_word}")
    print(f"Guesses remaining: {guesses_remaining}")
    user_guess = input('Please choose a letter: ')
    print(f"{masked_word} is the word you are trying to guess.")
    if user_guess in already_guessed:
        print(f"You already guessed the letter {user_guess}.")
        continue
    elif user_guess not in available_letters:
        print(f"{user_guess} is not a letter. Please try again.")
        continue
    else:
        print(f"You chose {user_guess}.")
        if user_guess not in list(choice):
            print(f"{user_guess} is not a letter in the word.")
            guesses_remaining -= 1
        else:
            print(f"{user_guess} is in the word!")
            new_masked_word = ''
            for x, y in zip(choice, masked_word):
                if user_guess == x:
                    new_masked_word += user_guess
                else:
                    new_masked_word += y
            masked_word = new_masked_word
        already_guessed.append(user_guess)
        available_letters.remove(user_guess)
        continue
