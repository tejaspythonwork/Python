# accept email/name/contact_number


from tkinter import *
import datetime
import os


def date_time_disp():
    
    dt = datetime.date.today()
    tm = datetime.datetime.now()
    tm_format = tm.strftime('%H:%M:%S')        
    dt_format = dt.strftime('%d-%m-%Y') 
    # print(dt)
    # print(tm)
    print(tm_format)
    print(dt_format)
    return tm_format,dt_format



def write_data_to_file(name,email,contact_number):
     formatted_time,formatted_date = date_time_disp()
     new_formatedd_time = formatted_time.replace(':','_')
     folder_path = rf'F:\Python\Python\Class_Assignment_AnjaliMaam\tkinter_example\student_info\{formatted_date}'
     print(new_formatedd_time)   
     filepath = rf'F:\Python\Python\Class_Assignment_AnjaliMaam\tkinter_example\student_info\{formatted_date}\{new_formatedd_time}.txt'

     if os.path.exists(folder_path):
         print(f'Folder Already Exists')
     else:
         os.mkdir(folder_path)
         print('Folder has been created')   

     with open(filepath, 'w+') as f1 :
        f1.write('\n=====================================')         
        f1.write('\n --------Student Information---------\n\n')
        f1.write(f'\nstudent name = {name}')
        f1.write(f'\nstudent email = {email}')
        f1.write(f'\nstudent contact number = {contact_number}')

    






def defination1():

    screen = Tk()

    screen.geometry('450x450')

    name_student = StringVar()
    email_student = StringVar()
    contact_number = StringVar()

    l1 = Label(text='Student Information')
    l1.place(x=180,y=0)


    name = Label(screen,text='Please enter name: ')
    name.place(x = 35,y=60)


    entry1 = Entry(screen,textvariable=name_student)
    entry1.place(x = 140,y= 60,)

    # ======
    email = Label(screen,text='Please enter email: ')
    email.place(x = 35,y=100)


    entry2 = Entry(screen,textvariable=email_student)
    entry2.place(x = 140,y= 100)        

    # ======

    contact = Label(screen,text='Please enter contact\nnumber: ')
    contact.place(x = 20,y=140)


    entry3 = Entry(screen,textvariable=contact_number)
    entry3.place(x = 140,y= 150)

    # ======

    
    btn1 = Button(screen,text='Write Data To File',bg='green',fg='white',command= lambda: write_data_to_file(name_student.get(),
                                                                                                    email_student.get(),
                                                                                                    contact_number.get()) )
    btn1.place(x = 170,y=250) 



    screen.mainloop()





defination1()
# date_time_disp()
# write_data_to_file('T','T','1')
