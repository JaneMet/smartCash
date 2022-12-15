#refact

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
        self.today = dt.date.today()

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        """Взять все рекорды за сегодня и посчитать сколько полчилось"""
        t_date = dt.date.today()

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if (self.week_ago <= record.date) and (self.week_ago <= self.today):
                week_stats.append(record.amount)
        return sum(week_stats)

    def get_today_limit_balance(self):
        """получить статистику за сегодня и сравнить с лимитом"""
        pass


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        """берем get_today_limit_balance и в зависимтоси от значения выводим комменатрий"""
        pass


class CashCalculator(Calculator):
    USD_RATE = 60.39
    EURO_RATE = 62.57
    RUB_RATE = 1

    def get_today_cash_remained(self, money):
        """берем get_today_limit_balance и в зависимтоси от значения выводим комменатрий"""


        # self.limit = 2500

        cash_remained = self.get_today_limit_balance()

        com_bad = 'Денег нет, держись'

        if cash_remained == 0:
            return com_bad

        money = {'usd': ('USD', CashCalculator.USD_RATE),
                 'eur': ('Euro', CashCalculator.EURO_RATE),
                 'rub': ('руб', CashCalculator.RUB_RATE)}


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
# дата в параметрах не указана, так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,comment='бар в Танин др',date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
print('test help')

