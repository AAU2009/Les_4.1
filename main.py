# This is a sample Python script.
import math
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """

    a="Привет"
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"{a}, {name}! Тебе {age} лет."
    print(output)

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = 2*(a+b)

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a*b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi*r**2

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2*math.pi*r

    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список

    a1 = random.randint (1,100)
    a2 = random.randint(1,100)
    a3 = random.randint(1,100)
    a4 = random.randint(1,100)
    a5 = random.randint(1,100)
    a6 = random.randint(1,100)
    a7 = random.randint(1,100)
    a8 = random.randint(1,100)
    a9 = random.randint(1,100)
    a10 = random.randint(1,100)
    print (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

    l = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    print(l)
    l.sort()
    print(l)
    print(l)

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы

    l = list(dict.fromkeys(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    print(d)

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
