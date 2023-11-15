import sqlite3
from tkinter.messagebox import showerror, showinfo


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


    def saving_error(self):
        showerror(title='Error', message='Не удалось сохранить результат.')
    def success(self):
        showinfo(title='Info', message='Результат сохранен.')
    
    def save_to_db(self, id:int, user_type:int, private:int=None):
        connection = sqlite3.connect('storage/test.db')
        cursor = connection.cursor()
        res = self.get_mistakes_num_of_mistakes_time()
        if user_type==0:#если обычный пользователь
            try:
            
                if len(res)//2==1:
                    print((id, 0, self.dim, res[0][1], res[0][2], private,))
                    cursor.execute("INSERT INTO user_results (user_id, date_time, num, dim, mistakes, duration, private)\
                                    values ((select id from users where name = ?), datetime('now'), ?, ?, ?, ?, ?);",
                                    (id, 0, self.dim, res[0][1], res[0][2], private,))
                    
                    connection.commit()
                else:
                    for i in range(len(res)//2):
                        cursor.execute("INSERT INTO user_results (user_id, date_time, num, dim, mistakes, duration, private)\
                                        values ((select id from users where name = ?), datetime('now'), ?, ?, ?, ?, ?);",
                                        (id, i+1, self.dim, res[i][1], res[i][2], private,))

                        connection.commit()
                self.success()
            except:
                 self.saving_error()

        else: #если пациент
            try:
                if len(res)//2==1:
                    print((id, 0, self.dim, res[0][1], res[0][2],))
                    cursor.execute("INSERT INTO patient_results (patient_id, date_time, num, dim, mistakes, duration)\
                                    values (?, datetime('now'), ?, ?, ?, ?);",
                                    (id, 0, self.dim, res[0][1], res[0][2],))
                    
                    connection.commit()
                else:
                    for i in range(len(res)//2):
                        cursor.execute("INSERT INTO patient_results (patient_id, date_time, num, dim, mistakes, duration)\
                                        values (?, datetime('now'), ?, ?, ?, ?);",
                                        (id, i+1, self.dim, res[i][1], res[i][2],))

                        connection.commit()
                self.success()
            
            except:
                self.saving_error()
        
        connection.close()