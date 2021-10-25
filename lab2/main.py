import colorama
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import init               #Пример использования стороннего pip-пакета
from colorama import Fore, Back, Style


def main():
    r = Rectangle("синего", 7, 8)
    c = Circle("зеленого", 3)
    s = Square("красного", 9.9)
    print(r)
    print(c)
    print(s)
    colorama.init()
    print(Back.RED + Fore.BLACK + 'Пример использования pip-пакета colorama')
    print(Back.YELLOW + Fore.BLACK + 'для установки выполнить pip install colorama')

if __name__ == "__main__":
    main()