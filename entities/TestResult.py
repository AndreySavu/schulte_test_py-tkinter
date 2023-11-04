class TestResult():
    def __init__(self, arrays_times, dimension):
        self.num_arrays_and_time = arrays_times
        self.dim = dimension
        self.mistakes_arr = []
        self.results = []
        for item in self.num_arrays_and_time:
            self.mistakes_arr.append(self.count_mistakes(item[0]))
        #self.get_mistakes_num_of_mistakes_time()
    
    def count_mistakes(self, array):
        mistakes = []
        for item in array:
            if array.count(item) > 1 and mistakes.count(item)==0:
                mistakes.append(item)
        
        return (mistakes, len(array)-self.dim**2)
    
    #массив с ошибочными номерами + количеством ошибок + время
    def get_mistakes_num_of_mistakes_time(self):
        for i,j in zip(self.num_arrays_and_time, self.mistakes_arr):
            self.results.append((j[0], j[1], i[1]))
        return self.results


    def save_to_db(self):
        pass