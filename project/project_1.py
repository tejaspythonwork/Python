# create folder dynamically with date if dont exists and
# create new seperate file based on information 
# of vaccination with hour - minute - second

from datetime import date, datetime 
import os

current_date = date.today()
c_f_date = current_date.strftime('%d-%m-%Y')
print(c_f_date)
current_time = datetime.now()
print(current_time)
formmated_current_time = current_time.strftime('%H:%M:%S')
f_c_t = formmated_current_time.replace(':','_')
print(f_c_t)
# ---------------------------------------------------------------

file_path = f'F:/Python/Python/project/{c_f_date}/{f_c_t}' + '.txt'
folder_path = f'F:/Python/Python/project/{c_f_date}'


def insert_vaccination_data():
    name = input('enter your name: ')
    email = input('enter email: ')
    gender = input('Enter gender: ')
    contact = input('Enter Contact: ')
    vac_type = input('Enter vaccination Type: ')
    vac_dose = input('Enter dose number: ')



    with open(file_path,'w') as f:
            f.write(f'\n--------------- {c_f_date} -------------------')
            f.write(f'\n--------------- {f_c_t} -------------------')    
            f.write(f'\n')
            f.write(f'\nyour name = {name}')
            f.write(f'\nyour email = {email}')
            f.write(f'\nyour gender = {gender}')
            f.write(f'\nyour contact = {contact}') 
            f.write(f'\nyour vac type = {vac_type}')
            f.write(f'\nyour dose number = {vac_dose}\n')
            f.write('---------------------------------------------------\n')
            f.close()




if os.path.exists(str(folder_path)):
    print('Folder Already Exists')
else:
    os.makedirs(str(folder_path))
    print('New Folder Has Been Created') 

insert_vaccination_data()