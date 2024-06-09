# takes list of words and returns length of longest word

words = []

def ninetine():
    max_length = 0
    max_word_name = ''
    status = True
    while status:
        words_input = input('Enter Words: ')
        words.append(words_input)

        choice = input('do you want to enter more words press y for yes and n for no: ')
        if choice == 'y' or choice == 'yes' or choice == '' :
            status = True
        elif choice == 'n' or choice == 'no':
            status = False
            print(words)
            for w in words:
                word_lenght = len(w)
                if word_lenght > max_length:
                    max_length = word_lenght
                    max_word_name = w
            print(f'Max Length = {max_length}')
            print(f'Max Length Word = {max_word_name}')

ninetine()        