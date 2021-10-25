import random

def gen_random(num_count, begin, end):          #Генератор определенного количества случайных чисел
    for i in range(num_count):
        yield random.randint(begin, end)        #Использование пакета для генерации случайных переменных и метода для целых чисел

if __name__ == '__main__':
    print(str(list(gen_random(5, 1, 4)))[1:-1])
