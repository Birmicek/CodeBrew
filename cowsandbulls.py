import random

def generate_number():
    a = 0
    generated_number_list = []
    while a == 0:
        a, b, c, d = random.sample(range(10), 4)
        generated_number_list.append(str(a))
        generated_number_list.append(str(b))
        generated_number_list.append(str(c))
        generated_number_list.append(str(d))
    return generated_number_list

def guess():
    generated_number_list = generate_number()
    #print(generated_number_list)
    guess_count = 0
    
    print("Hello there!\n"
          "I've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.\n"
          "Enter a number")
    guess_number = list(input('>>>'))
    
    while len(guess_number) != 4:
        print('You have to enter 4 digits number. Please try again.')
        guess_number = list(input('>>>'))

    guess_count += 1

    if guess_number == generated_number_list:
        print(f"Correct, you've guessed the right number in {guess_count} guesses!")
        exit()

    while guess_number != generated_number_list:
        cows_count = 0
        bulls_count = 0
        for i in range(0, len(guess_number)):
            if guess_number[i] == generated_number_list[i]:
                bulls_count += 1
            elif guess_number[i] in generated_number_list:
                cows_count += 1
        print(f'{bulls_count} bulls, {cows_count} cows')
        guess_number = list(input('>>>'))
        
        while len(guess_number) != 4:
            print('You have to enter 4 digits number. Please try again.')
            guess_number = list(input('>>>'))

        guess_count += 1
        #print(f'Your guess count is: {guess_count}')
        
    print(f"Correct, you've guessed the right number in {guess_count} guesses!")       

if __name__ == '__main__':
    guess()