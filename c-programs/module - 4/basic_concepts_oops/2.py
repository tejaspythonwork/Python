# define a class to represent a bank account 

class SBIBank:
    
  def  __init__(self):
    self.name_of_depositor = input('Enter Name of dipositor: ')
    self.account_number = input('Enter Account Number: ')
    self.type_of_account = input('Enter Type Of Account: ')
    self.balance_amount = 5000
    # self.total_amount = 0



  def diposit_amount(self):
    self.dip_amount = int(input('Enter amount for deposit: '))
    self.total_amount = self.balance_amount + self.dip_amount   
    print(f'Total Amount Balance = {self.total_amount}')


  def withdraw_amount(self):
    self.witdraw_amt = int(input('Enter Amount to widraw: '))
    if self.total_amount >= self.witdraw_amt:
      remaining_amount = self.total_amount - self.witdraw_amt
      print(remaining_amount) 
      return remaining_amount
    else:
      print('Insufficient Amount')
      return self.total_amount

  def disp_name_balance(self):
    print(f'Your name - {self.name_of_depositor}')
    print(f'Your balance - {self.withdraw_amount()}')    

obj = SBIBank()    
obj.diposit_amount()
# obj.withdraw_amount()
obj.disp_name_balance()