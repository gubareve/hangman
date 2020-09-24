def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def numbered_words(english_words, number):
    result = []
    for word in english_words:
        if len(word) == number:
            result.append(word)
    return result

def lettered_words(english_words, position, letter):
    result = []
    for word in english_words:
        if list(map(str, word))[position-1] == letter:
            result.append(word)
    return result

def common_letter(words, *letters):
    data = {}
    if letters:
        for letter in letters[0]:
            words = [word.replace(letter, '') for word in words]
    for word in words:
        letters = set(word)
        for letter in letters:
            try:
                data[letter] = word.count(letter) + data[letter]
            except:
                data[letter] = word.count(letter)
    key, value = max(data.items(), key=lambda x:x[1])
    return key

def doesnt_include(words,letters):
    result = []
    for word in words:
        if len(set(letters).intersection(map(str, word))) == 0:
            result.append(word)
    return result

def start():
    try:
        words = load_words()
        number_of_letters = int(input('How many letters are on the board:\n>> '))
        # get a array of all words with x letters:
        words = numbered_words(words, number_of_letters)
        print('The most common letter for words with that amount of letters is: '+common_letter(words))
        letters = ()
        wrong_letters = []
        while True:
            position = int(input('Enter the position of the letter:\n>> '))
            letter = input('Enter the letter:\n>> ')
            words = lettered_words(words,position,letter)
            print(words)
            letters = list(letters)
            letters.append(letter)
            letters = tuple(letters)
            try:
                print('The most common letter is '+common_letter(words, letters)+' so guess that :).')
                while True:
                    if input('Is that correct? (y/n)\n>> ') == 'n':
                        wrong_letters.append(common_letter(words, letters))
                        print('You should try '+common_letter(doesnt_include(words,wrong_letters),letters))
                        if input('Is that correct? (y/n)\n>> ') == 'n':
                            wrong_letters.append(common_letter(doesnt_include(words,wrong_letters),letters))
                            print('You should try '+common_letter(doesnt_include(words,wrong_letters),letters))
                        else:
                            break
                    else:
                        break

            except Exception as e:
                print(e)
                break
    except:
        print('Oops a error happened')