import random

all_words = ['Mother', 'gaMe', 'wiNter', 'lOVe', 'hOckey', 'compUTer', 'weaTher']

def choose_word():
    word = random.choice(all_words)
    #print(word)
    return word

def guess():
    guess_count = 9
    word = choose_word().lower()
    print(word)
    print('I am thinking of a word. What word is it?:\n')
    letter_count = len(word) * '_ '
    print(letter_count)
    letter_count = letter_count.split(' ')
    print()
    user_guess = input(f'Guess a letter ({guess_count} guesses is available): ')
    user_guess = user_guess.lower()

    while len(user_guess) != 1:
        print()
        print('You have to enter 1 letter!')
        print()
        user_guess = input(f'Guess a letter ({guess_count} guesses is available): ')
        user_guess = user_guess.lower()

    while guess_count > 0:
        if user_guess in word:
            ind = word.index(user_guess)
            letter_count[ind] = user_guess
            letter_count = ' '.join(letter_count)
            print(letter_count)
            letter_count = list(letter_count)
            guess_count -= 1
        user_guess = input(f'Guess a letter ({guess_count} guesses is available): ')
        user_guess = user_guess.lower()




if __name__ == '__main__':
    guess()
