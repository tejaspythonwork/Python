# check string is binary or notd

def defination13(text_str):

    dgt = set(text_str)
    s = {0,1}

    if s == dgt or dgt == {0} or dgt == {1}:
        print('Yes')
    else:
        print('No')


defination13({0,1,1})