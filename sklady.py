import re

vowels = set('аеиоіуєїюя')
sign_chars = set('ь')
pattern_str = "(c*[ь]?vc+[ь](?=v))|(c*[ь]?v(?=v|cv))|(c*[ь]?vc[ь]?(?=cv|ccv))|(c*[ь]?v[cь]*(?=$))"
pattern = re.compile(pattern_str)


def get_syllables(word):
    mask = ''.join(['v'
                    if c in vowels
                    else c
                        if c in sign_chars
                        else 'c'
                    for c in word.lower()])
    return [word[m.start():m.end()] for m in pattern.finditer(mask)]


word = input('ВВедіть слово:')
print('-'.join(get_syllables(word)))