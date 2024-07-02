# dictionary = 10 questions with 4 answer and 1 right answer as key
wrong_answer_count = 0
marks = 0
correct_answer_count = 0
def question_answer(dictionary_key_val,que_number):
    global marks
    global correct_answer_count
    global wrong_answer_count
    print(f'Question {que_number}. {dictionary_key_val['Que']}')
    print(f'Please select answer:')    
    for k,v in dictionary_key_val['answer'].items():
          print(f'{k}. {v}')  

    answer_for_q1 = int(input('please enter answer: '))
    print(f'{dictionary_key_val['correct_answer']}')
    if answer_for_q1 == dictionary_key_val['correct_answer']:
         print('Correct Answer')
         marks = marks + 50
         correct_answer_count = correct_answer_count + 1
    else:
         print('Wrong Answer')     
         marks = marks - 50
         wrong_answer_count = wrong_answer_count + 1




def question1():
    dictionary1 = {'Que' : 'Most Popular Backend Prgramming Language','answer' : {1 : 'Python',2:'Java' ,
                                                                                  3:'Mongo DB',4:'Java Script'},
                                                                                  'correct_answer' : 1}

    question_answer(dictionary1,1)    


def question2():
    dictionary2 = {'Que' : 'Which is giant animal','answer' : {1 : 'Horse',2:'Dog' ,
                                                             3:'Cat',4:'Elephant'},
                                                            'correct_answer' : 4}
     

    question_answer(dictionary2,2)



def question3():
    dictionary3 = {'Que' : 'Which animal Can Barking','answer' : {1 : 'Horse',2:'Dog' ,
                                                             3:'Cat',4:'Elephant'},
                                                            'correct_answer' : 2}
     
    question_answer(dictionary3,3)


def question4():
    dictionary4 = {'Que' : 'Who is best cricketer','answer' : {1 : 'Ms.Dhoni',2:'Virat Kohali' ,
                                                             3:'Ravindra Jadeja',4:'Honey Singh'},
                                                            'correct_answer' : 1}
     
    question_answer(dictionary4,4)


def question5():
    dictionary5 = {'Que' : 'Who is host of KBC','answer' : {1 : 'SRK',2:'Rithik' ,
                                                             3:'Amitabh',4:'Ajay'},
                                                            'correct_answer' : 3}
     
    question_answer(dictionary5,5)


def question6():
    dictionary6 = {'Que' : 'Who is elderest Actor ','answer' : {1 : 'SRK',2:'Rithik' ,
                                                             3:'Amitabh',4:'Ajay'},
                                                            'correct_answer' : 3}
     
    question_answer(dictionary6,6)


def question7():
    dictionary7 = {'Que' : 'What is 2 + 3 ','answer' : {1 : '1',2:'2' ,
                                                             3:'10',4:'5'},
                                                            'correct_answer' : 4}
     
    question_answer(dictionary7,7)


def question8():
    dictionary8 = {'Que' : 'What is 250 * 250','answer' : {1 : '10',2:'62500' ,
                                                             3:'1200',4:'350'},
                                                            'correct_answer' : 2}
     
    question_answer(dictionary8,8)

def question9():
    dictionary9 = {'Que' : 'What is 1.2 + 3.8','answer' : {1 : '5.0',2:'11.11' ,
                                                             3:'dont know',4:'4353'},
                                                            'correct_answer' : 1}
     
    question_answer(dictionary9,9)


def question10():
    dictionary10 = {'Que' : 'From answer which name is start with number',
                                                'answer' : {1 : 'SRK',2:'12345ABC' ,
                                                             3:'Amitabh',4:'Ajay'},
                                                            'correct_answer' :2}
     
    question_answer(dictionary10,10)


def defination_print():
    print('Welcome To The KBC')
    print('This Game is with 10 Questions')
    print('When your answer is correct you will get 50 points\nand if answer is wrong you will lose 50 points')
    print('After Game Completed You will get your score of \nhow much you have give correct and wrong answers')
    print('Lets Begin')
    question1()
    question2()
    question3()    
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()    
    print('===============================================')
    print('Game is Finished')
    print(f'Your Score = {marks}')
    print(f'Correct Answer = {correct_answer_count}')
    print(f'Wrong Answer = {wrong_answer_count}')
    print('===============================================')



defination_print()    