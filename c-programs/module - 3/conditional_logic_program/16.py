# temprature in centigrade and print statment accordingly
centigrade = int(input('Read temprature in centigrade: '))

def temparature():
    if centigrade < 0:
        return 'Freezing Weather'
    elif centigrade > 0 and centigrade <=10:
        return 'Very Cold Weather'
    elif centigrade > 10 and centigrade <=20:
        return 'Cold Weather'
    elif centigrade > 20 and centigrade <=30:
        return 'Normal In Temparatue'
    elif centigrade > 30 and centigrade <=40:
        return 'its hot'
    else:
        return 'Its very hot'  


temp = temparature()
print(temp)