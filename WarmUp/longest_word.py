words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

def char_counter():
    char_numb = 0
    for i in words:
        if len(i) > char_numb:
            char_numb = len(i)
            longest_word = i

    print(tuple([longest_word, char_numb]))

char_counter()