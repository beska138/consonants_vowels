word = input('Print a line:')
def cons_vow (word):
    dict = {'а':'v','б':'c','в':'c','г':'c','ґ':'c','д':'c','е':'v',
            'ж':'c','з':'c','у':'v','і':'v','к':'c','л':'c','м':'c','н':'c',
            'о':'v','п':'c','р':'c','с':'c','т':'c','и':'v','ф':'c','х':'c',
            'ц':'c','ч':'c','ш':'c','щ':'cc','я':'v','ю':'v','є':'v','ї':'v',
            'й':'c','ь':'','`':'*','А':'V','Б':'C','В':'C','Г':'C','Ґ':'C','Д':'C',
            'Е':'V','Ж':'C','З':'C','У':'V','І':'V','К':'C','Л':'C','М':'C','Н':'C',
            'О':'C','П':'C','Р':'C','С':'C','Т':'C','И':'V','Ф':'C','Х':'C','Ц':'C',
            'Ч':'C','Ш':'C','Щ':'CC'}

    dict_0 = {'Я':'Cv','Ю':'Cv','Є':'Cv','Ї':'Cv','Й':'C','я': 'cv',
              'ю': 'cv', 'є': 'cv', 'ї': 'cv', 'й': 'c'}
    if word[0] in "ЯЮЄЇЙяюєїй":
        word = word.replace(word[0], dict_0[word[0]])
    for letter in word:
        if letter in dict.keys():
            word = word.replace (letter, dict [letter])
    return word
print (cons_vow(word))