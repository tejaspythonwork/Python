# merge dictionaries with custom aggregation

def defination80():
     sales   = {'product1': 100,  'product2':150} 
     returns = {'product1': 20, 'product2': 30} 
     d1 = {'product1': 20, 'product2': 10} 

     merged = {k:sales.get(k,0) + returns.get(k,0) + d1.get(k,0) for k in sales | returns | d1}
     print(merged)

defination80()     