# find key with specific value

def defination24():
    grades = {'math': 90, 'history': 85, 'science': 90}
    fun1 = lambda x:x[1] == 90
    fun2 = dict(filter(fun1,grades.items()))
    print(fun2)


defination24()