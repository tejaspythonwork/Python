# merge dictionaries with aggregation


def defination49():
     aggregate = {}
     sales_q1 = {'apple': 50, 'banana': 30} 
     sales_q2 = {'apple': 60, 'banana': 20, 'cherry': 40}

     for k,v in sales_q1.items():
          aggregate[k] = v


     for k1,v1 in sales_q2.items():
          if k1 in aggregate:
               aggregate[k1] +=v1 
          else:
               aggregate[k1] = v1           


     print(aggregate)

defination49()     