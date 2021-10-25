def field(items, *args):        #items - список словарей, args - аргументы - ключи словаря
    
    assert len(args) > 0
    if len(args) == 1:          #Если передан один элемент - выдаются только соответствующее значение для ключа словаря
        for i in items:
            if args[0] in i.keys() and not i[args[0]] is None:          #Проверка на наличие ключа в данном словаре и на отсутствие значения None для поля          
                yield i[args[0]]
    else:                       #Если передано несколько аргументов
        for i in items:
            tmp_dict = {}      #Временный локальный словарь для заполнения и вывода
            for key in args:
                if key in i.keys() and not i[key] is None:
                    tmp_dict[key] = i[key]
            if len(tmp_dict) > 0:
                yield tmp_dict


if __name__ == '__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
    ]   
    print(str(list(field(goods, 'title')))[1:-1])
    print(str(list(field(goods, 'title', 'price')))[1:-1])
