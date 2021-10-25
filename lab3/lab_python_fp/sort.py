data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print('Без использования lambda-функции: ', sorted(data, key=abs, reverse=True))
    print('С использованием lambda-функции: ', sorted(data, key = lambda x: x if x >= 0 else -x, reverse=True))
