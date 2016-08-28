import random


def generate_random_word():
    words = ['apple', 'orange', 'banana']
    word = words[random.randint(0, len(words) - 1)]
    return word


def print_word(blank_word):
    for letter in blank_word:
        print(letter, " ", end="")
    print("")


def get_guess_letter():
    print("Type letter")
    letter = input()
    return letter


def process_letter(letter, secret_word, blank_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blank_word[i] = letter

    return result


def print_attempts(number_of_attempts):
    for i in range(0, number_of_attempts):
        print("X", end="")
    print("")


def guess_word_game():
    attempts = 0
    max_attempts = 5
    can_play = True

    word = generate_random_word()
    blank_word = list("_" * len(word))

    while can_play:
        print_word(blank_word)
        letter = get_guess_letter()
        found = process_letter(letter, word, blank_word)

        if not found:
            attempts += 1
            print_attempts(attempts)

        if attempts >= max_attempts:
            can_play = False

        if not "_" in blank_word:
            can_play = False

    if attempts >= max_attempts:
        print("You loose:(")
    else:
        print("Winner:)")

print("Game started")
guess_word_game()
print("Game over")