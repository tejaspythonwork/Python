import datetime


def date_and_time(self):
   dt = datetime.date.today()
   tm = datetime.datetime.now()
   tm_format = tm.strftime('%H:%M:%S')        
   dt_format = dt.strftime('%d-%m-%Y')      
#    print(dt)
#    print(dt_format)
#    print(tm_format)
   return dt_format,tm_format 
