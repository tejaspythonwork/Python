# python program to find number of vowels in string


def defi9(input_str):
    present_vowels = []
    absent_vowels = []
    vowels = 'aeiouAEIOU'.lower()
    count = 0
    
    
    for char in input_str:
        if char in vowels:
            count += 1
            if char not in present_vowels:
                present_vowels.append(char)
    
    
    for vowel in vowels:
        if vowel not in present_vowels:
            absent_vowels.append(vowel)
    
    return count, present_vowels, absent_vowels


# input_str = "Geeks For Geeks"
# c, present_vw, absent_vw = defi9(input_str)

# print(f"Number of vowels present: {c}")
# print(f"Vowels present: {present_vw}")
# print(f"Vowels absent: {set(absent_vw)}")


def def9(str):
    present_vowels = []
    absent_vowels = []
    vowels = 'aeiouAEIOU'
    count = 0

    for char in str:
     if char in vowels:
         count = count + 1
         if char not in present_vowels:
             present_vowels.append(char)
    
    for vowel in vowels:
        if vowel not in present_vowels:
            absent_vowels.append(vowel)
    
    return count,present_vowels,absent_vowels


res_count,present_vowels,absent_vowels = def9('Geeks For Geeks')
print(res_count)
print(f'Present Vowels = {present_vowels}')
print(f'Absent Vowels =  {absent_vowels}')