# count the occurences of each word 
# in given sentence

sentence = "This is simple sentence to count words this"

def count_words(statments):
    words = sentence.lower().split()
    words_count = {}
    for w in words:
        if w in words_count:
            words_count[w] = words_count[w] + 1
            print(f'WORD COUNT = {w}')
            print(f'words_count = {words_count}')
        else:
            words_count[w] = 1

    return words_count
word_count = count_words(sentence)    
print(f'Word count for sentence = {sentence}') 
for w,c in word_count.items():
    print(f'\t{w} : {c}')  