sentence = 'a speech sound that is produced by comparatively open configuration of the vocal tract'

vows = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'Y': 0 }
consts = {}

def vow_const_count():
    for i in sentence:
        if not i.isalpha():
            pass
        elif i in vows.keys():
            vows[i] += 1
        else:
            if i in consts.keys():
                consts[i] += 1
            else:
                consts[i] = 1 

    vows_count = sum(vows.values())
    const_count = sum(consts.values())
    print(f'No. consonants: {const_count} | No. vowels: {vows_count}')

vow_const_count()