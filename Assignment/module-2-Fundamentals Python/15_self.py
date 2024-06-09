# 
sentence = "This is simple sentence to count words this"

def words(statment):
    w = statment.lower().split(' ')
    words_count = {}
    # print(f'{w}')
    for st in w:
        if st in words_count:
            words_count[st] = words_count[st] + 1
            print(f'WORD COUNT = {w}')
            print(f'words_count = {words_count}')
            print(st)
        else:
            words_count[st] = 1
            print('---')
            print(w)
            print(words_count)
            print('---')

words(sentence)