# write a program to copy content of one file to another file

from datetime import datetime,date

now = date.today()
now_time = datetime.now()
current_time = now_time.strftime('%H:%M:%S')
print(current_time)
formatted_now = now.strftime('%d-%m-%Y')
print(formatted_now)

source_file_name = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt'
destination_file_name = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_2_copy.txt'

with open(source_file_name,'r') as fl:
    content = fl.read()
    fl.close()

with open(destination_file_name,'w') as fl2: 
    content1 = fl2.write(content+'\n')
    fl2.write(formatted_now+'\n')
    fl2.write(current_time+'\n')
    print('Content Has Been Copied\n')
    print(f'\n on date = {formatted_now}'.strip())
    print(f'\n on time = {current_time}\n'.strip())
    fl2.close()   
