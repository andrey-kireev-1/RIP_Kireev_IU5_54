
def print_result(func):             #Декоратор для print_result
    def decorated_func(*args):  
        print(func.__name__)
        return_value = func(*args)  #Вызов исходной функции
        if isinstance(return_value, list):  #Проверка является ли результат списком
            for value in return_value:
                print(str(value))
        elif isinstance(return_value, dict):    #Проверка является ли результат словарем
            
            for key in return_value.keys():
                print(str(key) + ' = ' + str(return_value[key]))
            
        else:
            print(return_value)     #Если не словарь и не список, то переменная
        return return_value
    return decorated_func




@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('______________')

    test_1() 
    test_2()
    test_3()
    test_4()