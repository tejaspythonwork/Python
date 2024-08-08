# find longest word in a file

filename = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt'
def find_longest_word(wrd):
    max_length = max(map(len,wrd))
    return filter(lambda word : len(word) == max_length,wrd)


with open(filename,'r') as f: 
    content = f.read()
    words = [wrd.strip() for wrd in content.split()]
    longest_word = list(find_longest_word(words))

    print(f'Longest Word - {longest_word}')
    f.close()