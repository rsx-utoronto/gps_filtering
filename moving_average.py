class GPS:
    def __init__(self, n=50):
        self.n = n
        self.i = 0
        self.data = [0] * self.n
        self.sum = 0
        self.average = 0
        
    def add_avg(self, new_data):
        self.data.append(new_data)
        self.sum = self.sum + new_data - self.data.pop(0)
        if self.i < self.n:
            self.i += 1
            return new_data
        else:
            self.average = self.sum / self.n
            return self.average
    
    def print_list(self):
        print (self.data)
        
    def reset(self, n):
        self.n = n
        self.i = 0
        self.data = [0] * self.n
        self.sum = 0
        self.average = 0
