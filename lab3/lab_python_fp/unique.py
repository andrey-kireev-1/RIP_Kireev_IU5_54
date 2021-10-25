import random

class Unique:

    def __init__(self, items, **kwargs):            #Конструктор класса
        self.used_el = set()                        #Множество уже использованных элементов
        self.data = list(items)                     #Список с данными для проверки
        self.index = 0                              #Индекс для прохода по списку с данными
        if 'ignore_case' in kwargs.keys() and kwargs['ignore_case'] == True:    #Проверка на учет регистра
            self.ignore_case = True
        else:
            self.ignore_case = False

    def __next__(self):                             #Метод следующего элемента
        while True:
            if self.index >= len(self.data):        #Если еще есть данные в списке
                raise StopIteration
            cur = self.data[self.index]
            self.index += 1
            if ((self.ignore_case or not isinstance(cur, str)) and cur not in self.used_el):    #Проверка является ли cur элементом класса и был ли он уже использован
                self.used_el.add(cur)
                return cur
            elif (not self.ignore_case and isinstance(cur, str)     #Учет регистра
                    and cur.upper() not in self.used_el
                    and cur.lower() not in self.used_el):
                self.used_el.add(cur.upper())
                self.used_el.add(cur.lower())
                return cur

    def __iter__(self):         #Метод итератор
        return self


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    data_int = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data_rand = gen_random(10, 3, 10) 
    data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Отбор уникальных чисел: ', str(list(Unique(data_int)))[1:-1])
    print('Отбор уникальных случайных чисел: ', str(list(Unique(data_rand)))[1:-1])
    print('Отбор уникальных строк без игнорирования регистра по умолчанию: ', str(list(Unique(data_str)))[1:-1])
    print('Отбор уникальных строк (регистр учитывается): ', str(list(Unique(data_str, ignore_case=True)))[1:-1])
    print('Отбор уникальных строк (регистр НЕ учитывается): ', str(list(Unique(data_str, ignore_case=False)))[1:-1])