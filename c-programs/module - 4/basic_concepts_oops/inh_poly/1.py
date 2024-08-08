class Cricketer:
    pass


class Batsman(Cricketer):
    # performance:
    # 1 - low
    # 2 - medium
    # 3 - best

    def __init__(self):
        self.total_runs = 500
        self.avg = 1500
        self.performance = 3
        

    def input_data(self): 
        self.total_runs = int(input('Please enter total runs: ')) 
        self.total_avg = int(input('Please enter average: '))    
        self.performance = int(input('Please enter performance: ')) 

    def display_data(self):
        print(f'{self.total_runs}') 
        print(f'{self.avg}') 
        print(f'{self.performance}')    


obj = Batsman()
obj.input_data()
obj.display_data()