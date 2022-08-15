def swap_if_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return letter.swapcase()
    return letter


def swap_vowel_case(st):
    return ''.join([swap_if_vowel(x) for x in list(st)])
