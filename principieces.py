class SomeClass(object):
    attr1 = 42

    def method1(self, x):
        return 2*x


obj = SomeClass()
obj.method1(6) # 12
obj.attr1 # 42


print("ООО Медовый Гексагон")
print("Мёд липовый", end=" ")
print(1, end="шт ")
print(1250, end="р")
print("\nCумма", 1250, end="р")
print("\nСпасибо за покупку!")


def print_check(honey_positions):
    sum = 0  # переменная для накопления общей суммы
    print("ООО Медовый Гексагон\n")
    # в цикле будем выводить название, количество и цену
    for honey in honey_positions:
        name = honey[0]
        amount = honey[1]
        price = honey[2]
        print(f"{name} ({amount} шт.) - {price} руб.")
        sum += amount * price  # здесь же будем считать ещё и общую сумму
    print(f"\nИтого: {sum} руб.")
    print("Спасибо за покупку!")


# (название, количество, цена за штуку)
honey_positions = [
    ("Мёд липовый", 3, 1250),
    ("Мёд цветочный", 7, 1000),
    ("Мёд гречишный", 6, 1300),
    ("Донниковый мёд", 1, 1750),
    ("Малиновый мёд", 10, 2000),
]

print_check(honey_positions)

print ("---------------------")


def int_multiple(a, b):
    product = a * b
    # возвращаем значение
    return int(product)


print(int_multiple(341, 2.7))

print ("---------------------")
num = 42


def some_function(n):
    res = n + num
    return res


print(some_function(1))

print ("---------------------")
from abc import ABC, abstractmethod


class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")


class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")


# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))
#https://www.askpython.com/python/oops/abstraction-in-python на англ статья
# https://pythobyte.com/abstraction-in-python-2759e6c7/ на русском - условный перевод

print('---------------------------')

#https://smartiqa.ru/courses/python/lesson-6 принципы ООП ниже

