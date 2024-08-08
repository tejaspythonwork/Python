# accept 5 numbers and display it
status = True 

while status:
   input_string = input('Enter list of integers seperated by spaces: ')
   
   if(len(i_var)==5):
      print()
   else:
      i_var = list(map(int,input_string.split()))  
for n in i_var:
   print(n)   