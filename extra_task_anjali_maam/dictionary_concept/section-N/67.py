# group by dictionary values

def defination67():
     entries = [
          {'category': 'fruit','item': 'apple'}, 
          {'category': 'fruit', 'item':'banana'}, 
          {'category': 'vegetable', 'item': 'carrot'}
          ]
     
     new_dict = {}

     for entry in entries:
          cat = entry['category']
          itm = entry['item']


          if cat in new_dict:
               new_dict[cat].append(itm) 
          else:
               new_dict[cat] = [itm] 

     print(new_dict)                  



defination67()              