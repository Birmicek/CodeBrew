def echo():
    repetition = int(input("Enter the number of repetitions: "))
    sentence = input("Enter the sentence: ").split(' ')
    for i in sentence:
        final_out = repetition * i.split(' ')
        x = ' '.join(final_out)
        print(x, end=' ')

echo()


