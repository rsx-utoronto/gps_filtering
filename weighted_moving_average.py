## used a linear weight distribution
class GPS:
    def __init__(self, n=50):
        self.n = n
        self.data = []
        self.average = 0
        
    def add_avg(self, new_data):
        self.data.append(new_data)
        if len(self.data) > self.n:
            self.data.pop(0)
        length = len(self.data)
        average = 0
        
        for i in range(length):
            weight = (i+0.5)/(length * (length*1/2.0)) ##normalized by area of n by 1 triangle
            average += self.data[i]*weight
        self.average = average
        return average

    def print_data(self):
        print ("list: "+str(self.data)+"\naverage: "+str(self.average))
        
    def reset(self, n):
        self.n = n
        self.data = []
        self.average = 0
