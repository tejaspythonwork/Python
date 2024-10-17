# retrieve key - val pair as tuple

def defination23():
    person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    person1 = [(k,v) for k,v in person.items()]
    print(tuple(person1))

    # remove outer round braces

    for i in person1:
        print(i)

defination23()    