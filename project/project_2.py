import math as math

class Project2:
    status = True   
    def __init__(self):
        self.name = ''
        self.qty_of_pizza = 0
        self.qty_of_pasta = 0
        self.main_menu = '''
                    Menu
                press - 1:Order Menu
                press - 2:Exit  
                '''
        
        self.large_pizza_1 = 10.99
        self.large_pizza_2 = 20.99
        self.large_pizza_3 = 29.99
               


        self.large_pasta_1 = 9.5
        self.large_pasta_2 = 17.00
        self.large_pasta_3 = 27.50
            


    def display_menu(self):
        order_menu = '''
                Pizza Menu
        ==============================    
        1. 1 Large Pizza = 10.99 AUD        
        2. 2 Large Pizza = 20.99 AUD
        3. 3 Large Pizzza = 29.99 AUD

        *** Buy 4 or more pizzas and get 1.5 ltr of soft drink free ***

                Pasta Menu  
        =============================
        1. 1 Large Pasta = 9.5 AUD
        2. 2 Large Pasta = 17.00 AUD
        3. 3 Large Pasta = 27.50 AUD
        
        *** Buy 4 or more pastas and get 2 bruschetta Free ***
        *** Buy 4 or more pizzas and pastas and get 2 choco brownies ice cream free   
        
        '''
        return order_menu



    def set_customer_name(self,name):
        self.name = name

    def get_customer_name(self):
        return self.name
    
    def set_pizza_qty(self,pizza_qty=0):
        self.qty_of_pizza = pizza_qty

    def get_pizza_qty(self):
        return self.qty_of_pizza
    
    def set_pasta_qty(self,qty_pasta=0):
        self.qty_of_pasta = qty_pasta

    def get_pasta_qty(self):
        return self.qty_of_pasta

    def get_order_details(self):
        
        # =========
        self.name = input('Please enter customer name: ')
        self.set_customer_name(self.name)
        # =========
        self.qty_of_pizza = int(input('Please enter quantity of pizza: '))
        self.set_pizza_qty(self.qty_of_pizza)
        # =========
        self.qty_of_pasta = int(input('Please enter quantity of pasta: '))    
        self.set_pasta_qty(self.qty_of_pasta)

    def set_calculate_price_pizza_pasta(self):
        self.total_price_pizza = self.get_pizza_qty() * 10.99
        self.total_price_pasta = self.get_pasta_qty() * 9.5

    def get_total_price_pizza(self):
        return self.total_price_pizza
    
    def get_total_price_pasta(self):
        return self.total_price_pasta

    def give_soft_drink_free(self):
        if self.get_pizza_qty() >= 4:
        #    print('Congratulation !! 1.5ltr soft drink is free')
           return 'Congratulation !! 1.5ltr soft drink is free' 
        else: 
           return 

    def give_bruschetta_free(self):
        if self.get_pasta_qty() >= 4:
        #    print('Congratulation  !! 2 bruschetta Free')
           return 'Congratulation  !! 2 bruschetta Free'
        else:
            return

    def give_2_choco_brownie_icecream_free(self):
        if self.get_pizza_qty() >=4 and self.get_pasta_qty() >=4:
        #   print( 'Congratutalion 2 choco brownie Icecream Free')
          return 'Congratutalion 2 choco brownie Icecream Free'
        else:
            return ''

    def print_details(self):
        print('=========================================================================')
        total_amount = self.get_total_price_pasta() + self.get_total_price_pizza()
        print(f'Customer Name = {self.get_customer_name()}')
        print(f'You have order quantity of pizza = {self.get_pizza_qty()}')
        print(f'You have order quantity of pasta = {self.get_pasta_qty()}')
        print(f'Total Price For Pizza = {self.get_total_price_pizza()}')
        print(f'Total Price For Pasta = {self.get_total_price_pasta()}')
        # self.give_soft_drink_free()
        soft_drink_msg = self.give_soft_drink_free()
        bruschetta_free = self.give_bruschetta_free()
        choco_brownie_free = self.give_2_choco_brownie_icecream_free()
        if soft_drink_msg:    
         print(self.give_soft_drink_free())
        if bruschetta_free: 
         print(self.give_bruschetta_free())
        if choco_brownie_free: 
         print(self.give_2_choco_brownie_icecream_free())
        
        print(f'Total Amount = {total_amount.__round__(2)} AUD')


    def fun_with_loop(self):
        total_count = 1
        while self.status:
         print(obj.display_menu())
         obj.get_order_details()
         obj.set_calculate_price_pizza_pasta()
         obj.print_details()
         obj.write_data_to_file()   
         total_pizza,total_pasta = obj.sum_total_pizza_pasta()
         print(f'Total Pizza Price In Entire File = {total_pizza}')
         print(f'Total Pasta Price In Entire File = {total_pasta}')

         total_pasta_sold,total_pizza_sold = obj.sum_count_of_pizza_pasta()
         print(f'Total Pasta Sold = {total_pasta_sold}')
         print(f'Total Pizza Sold = {total_pizza_sold}')
         soft_drink,browni,bruschetta = obj.count_soft_drink_browni()
         print(f'Total Soft Drink Sold = {soft_drink}')
         print(f'Total browni Sold = {browni}')
         print(f'Total bruschettas Sold = {bruschetta}')
         choice = input('Do you want to continue: ')
         if choice == 'y' or choice == 'yes':
             self.status = True
             total_count = total_count + 1   
         else:  
             self.status = False       
             print(total_count)

         

    def write_data_to_file(self):
        with open('abc.txt','a') as f:
            soft_drink_msg = self.give_soft_drink_free()
            bruschetta_free = self.give_bruschetta_free()
            choco_brownie_free = self.give_2_choco_brownie_icecream_free()
            total_amount = self.get_total_price_pasta() + self.get_total_price_pizza()
            print('---------------------------------------------------------')
            f.write(f'\nCustomer Name = {self.get_customer_name()}')
            f.write(f'\nPizza Quantity = {self.get_pizza_qty()}')
            f.write(f'\nPasta Quantity = {self.get_pasta_qty()}')
            f.write(f'\nTotal Pizza Price = {self.get_total_price_pizza()}')
            f.write(f'\nTotal Pasta Price = {self.get_total_price_pasta()}')
            # =====
            if soft_drink_msg:
              f.write(f'\n{soft_drink_msg}')
            # =====
            if bruschetta_free:
                f.write(f'\n{bruschetta_free}')
            # =====
            if choco_brownie_free:
                f.write(f'\n{choco_brownie_free}')
            f.write(f'\nTotal Amount = {total_amount.__round__(2)} AUD')
            f.write(f'\n======================================================')
            f.close()


    def sum_total_pizza_pasta(self):
      total_pizza_price_1 = 0
      total_pasta_price_1 = 0
      with open('abc.txt','r') as f: 
          for l in f:
             if l.startswith('Total Pizza Price'):
                price = float(l.split('=')[1].strip())
                total_pizza_price_1 = total_pizza_price_1 + price
             elif l.startswith('Total Pasta Price'):
                price = float(l.split('=')[1].strip())
                total_pasta_price_1 = total_pasta_price_1 + price
      return total_pizza_price_1,total_pasta_price_1   


    def sum_count_of_pizza_pasta(self):
       total_pizza_count = 0
       total_pasta_count = 0
       with open('abc.txt','r') as file:
          for line in file:
             if line.startswith('Pizza Quantity'):
                qty_pizza = float(line.split('=')[1].strip())
                total_pizza_count = total_pizza_count + qty_pizza
             elif line.startswith('Pasta Quantity'):
                qty_pasta = float(line.split('=')[1].strip())
                total_pasta_count = total_pasta_count + qty_pasta
       return total_pizza_count,total_pasta_count


    def count_soft_drink_browni(self):
       total_soft_drink = 0
       total_browni = 0
       total_bruschetta = 0
       with open('abc.txt','r') as file:
          for line in file:
             # for soft drink
             if 'soft drink' in line.lower():
                total_soft_drink = math.floor(float(line.split(' ')[2].replace('ltr','')))
                print(total_soft_drink)
                print('-----')
             if 'bruschetta' in line.lower():
                total_bruschetta = int(line.split()[2])
                print(total_bruschetta) 
                print('-----')
             if 'choco brownie' in line.lower():
                total_browni = int(line.split()[1])    
                print(total_browni)
                print('-----')
       return total_soft_drink,total_browni,total_bruschetta

obj = Project2()
'''================================================================='''
obj.fun_with_loop()

# total_pizza,total_pasta = obj.sum_total_pizza_pasta()
# print(f'Total Pizza Price In Entire File = {total_pizza}')
# print(f'Total Pasta Price In Entire File = {total_pasta}')

# total_pasta_sold,total_pizza_sold = obj.sum_count_of_pizza_pasta()
# print(f'Total Pasta Sold = {total_pasta_sold}')
# print(f'Total Pizza Sold = {total_pizza_sold}')
'''=================================================================='''
# obj.get_order_details()
# obj.give_soft_drink_free()
# obj.set_calculate_price_pizza_pasta()

# obj.print_details()
# obj.write_data_to_file()
# obj.count_soft_drink_browni()










