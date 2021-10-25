import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    try:
        coef = float(coef_str)
    except:
        error = 'error'
        return error
    return coef

def get_roots(a, b, c):
    results = []
    if a==0:
        if b==0:
            if c==0:
                print ("x - любое число\n")
                error = 'exception'
                return error
            else:
                print ('Уравнение вида {} = 0 не имеет решения'.format(c))
                error = 'exception'
                return error
        else:
            
            d=-c/b
            if d>0:
                results.append(-math.sqrt(d))
                results.append(math.sqrt(d))
            if d == 0:
                results.append(d)
    else:
        if b==0:
            if c==0:
                results.append(0)
            else:
                d=-c/a
                if d>0:
                    results.append(math.sqrt(math.sqrt(d)))
                    results.append(-math.sqrt(math.sqrt(d)))
        else:
            d=b*b-4*a*c
            if d==0:
                m=(-b)/(2*a)
                if m==0:
                    results.append(m)
                if m>0:
                    results.append(math.sqrt(m))
                    results.append(-math.sqrt(m))
            if d>0:
                m1=(-b+math.sqrt(d))/(2*a)
                m2=(-b-math.sqrt(d))/(2*a)
                if m1>0:
                    x1 = math.sqrt(m1)
                    x2 = -math.sqrt(m1)
                    if m2>0:
                        x3 = math.sqrt(m2)
                        x4 = -math.sqrt(m2)
                        results.append(x1)
                        results.append(x2)
                        results.append(x3)
                        results.append(x4)
                    if m2==0:
                        x3 = 0
                        results.append(x1)
                        results.append(x2)
                        results.append(x3)
                    if m2<0:
                        results.append(x1)
                        results.append(x2)
                if m1 == 0:
                    x1 = math.sqrt(m1)
                    if m2>0:
                        x3 = math.sqrt(m2)
                        x4 = -math.sqrt(m2)
                        results.append(x1)
                        results.append(x3)
                        results.append(x4)
                    if m2==0:
                        x3 = 0
                        results.append(x1)
                        results.append(x3)
                    if m2<0:
                        results.append(x1)
                if m1<0:
                    if m2>0:
                        x3 = math.sqrt(m2)
                        x4 = -math.sqrt(m2)
                        results.append(x3)
                        results.append(x4)
                    if m2==0:
                        x3 = 0
                        results.append(x3)
    return results



def main():
    '''
    Основная функция
    '''
    while True:
        a = get_coef(1, 'Введите коэффициент А:')
        b = get_coef(2, 'Введите коэффициент B:')
        c = get_coef(3, 'Введите коэффициент C:')
        if type(a) == float and type(b) == float and type(c) == float:
            break
        else:
            print('Введен неверный коэффициент. Повторите ввод коэффциентов.')
            
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    if roots == 'exception':
        return
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()