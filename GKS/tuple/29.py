# sort tuple alphabetically

def defination29():
    test_tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

    for i in range(len(test_tup)):
        for j in range(len(test_tup)-i-1):
            if test_tup[j][0] < test_tup[j + 1 ][0]:
                test_tup[j],test_tup[j + 1] = test_tup[j+1],test_tup[j]

    print(test_tup)


defination29()    