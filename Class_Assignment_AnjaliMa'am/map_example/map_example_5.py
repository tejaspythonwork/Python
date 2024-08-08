student = [
{
    'name' : 'Tejas', 'subject' : 'Python', 'score' : 75,
},

{
    'name' : 'Dhruv', 'subject' : 'Flutter', 'score' : 50
}

]

updated_student = list(map(lambda student:{'name':student['name'],'subject' : student['subject'],
                                           'score':student['score']+5},student))
print(updated_student)