import datetime as dt


class Record:

    def __init__(self, amount, comment):
        self.amount = amount
        self.comment = comment


class Calculator:

    def __init__(self, limit):
        pass

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        pass

    def get_week_stats(self):
        pass

    def get_today_limit_balance(self):
        pass
    

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
r1 = Record(amount=145, comment='Безудержный шопинг')
r2 = Record(amount=1568, comment='Наполнение потребительской корзины')
r3 = Record(amount=691, comment='Катание на такси')

# для CaloriesCalculator
r4 = Record(amount=1186, comment='Кусок тортика. И ещё один.', )
r5 = Record(amount=84, comment='Йогурт.')
r6 = Record(amount=1140, comment='Баночка чипсов.')

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


