from datetime import datetime as dt

class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if date is None:
            self.date = dt.today()
        else:
            self.date = dt.strptime(date,'%d.%m.%Y')

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        pass

    def get_week_stats(self):
        pass

    def get_today_limit_balance(self):
        t_limit_balance = self.limit - self.get_today_stats()
        return t_limit_balance
    

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        pass


class CashCalculator(Calculator):
    USD_RATE = 50.0
    EURO_RATE = 50.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        pass


# для CashCalculator
r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=1568,comment='Наполнение потребительской корзины',date='09.03.2019')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

# для CaloriesCalculator
r4 = Record(amount=1186,comment='Кусок тортика. И ещё один.',date='24.02.2019')
r5 = Record(amount=84, comment='Йогурт.', date='23.02.2019')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019')

# для CashCalculator
cash_calculator = CashCalculator(1000)
# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
print('test help')

