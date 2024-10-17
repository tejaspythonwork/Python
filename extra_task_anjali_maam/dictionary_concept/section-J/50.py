# group items by common values

def defination50():
    veg_dict = {}
    fruit_dict = {}
    entries = [
          {'category': 'fruit','item': 'apple'}, 
          {'category': 'fruit','item': 'banana'}, 
          {'category': 'vegetable', 'item': 'carrot'}
          ]
    
    for entr in entries:
        category = entr['category']
        item = entr['item'] 

        if category in fruit_dict:
            fruit_dict[category].append(item)
        else:
            fruit_dict[category] = [item]    

    print(fruit_dict)              

defination50()          

