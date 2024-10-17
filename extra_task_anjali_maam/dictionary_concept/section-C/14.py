# default dictionary

def defination14():
    counts = {'apple': 3, 'banana': 2}
    orange_count = counts.get('orange', 0)
    print("The count for 'orange' is:", orange_count)
    print(counts)
    print('-----setdefault method------')
    counts.setdefault('orange',1000)
    print(counts)

defination14()    