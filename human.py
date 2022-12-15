class Human:
#статические поля по заданию
    default_name = 'no name'
    default_age = 6

#2 публичных поля = динамические - обращаемся к объекту данного класса - self - берем из параметра слова
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
#создаем приватное свойство - не доступно вне класса, даже в классах-потомках
        self.__money = 0
        self.__house = None #жилье отсутствует

#4 справочный метод info
#обычный метод класса, поэтому в качесвте первого параметра принимает значение self
#принтим свойства, тк некоторые динамические - обращаемся через self
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

#5 - статический метод
#self не указывается, для работы не нужен
    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default name: {Human.default_age}')


#-----------
    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')


#6 - приватный метод - вне класса вызвать не можем
    def __make_deal(self, price, house):
        self.__money -= price
        self.__house = house


if __name__ == '__main__':
    print(Human.default_name)

# объект класса Человек, которому передают параметр - имя и возраст
    fedor = Human('Fedor', 32)
# 4 справочный метод info - вывод
    fedor.info()
    Human.default_info()
# -----------
    fedor.earn_money(203)
    fedor.info()
 #   a = 0

