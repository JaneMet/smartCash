import datetime as DT


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if date is None:
            self.date = DT.date.today()
        else:
            self.date = DT.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = DT.date.today()
        self.week_ago = self.today - DT.timedelta(days=7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        """Взять все рекорды за сегодня и посчитать сколько полчилось"""
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if (self.week_ago <= record.date) and (self.week_ago <= self.today):
                week_stats.append(record.amount)
        return sum(week_stats)

    def get_today_limit_balance(self):
        """получить статистику за сегодня и сравнить с лимитом"""
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        """берем get_today_limit_balance и в зависимтоси от значения выводим комменатрий"""
        calories_remained = self.get_today_limit_balance()
        if calories_remained > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                       f'калорийностью не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    USD_RATE = 60.39
    EURO_RATE = 62.57
    RUB_RATE = 1

    def get_today_cash_remained(self, money='rub'):
        """берем get_today_limit_balance и в зависимости от значения выводим комменатрий"""
        money_many = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}

        cash_remained = self.get_today_limit_balance()

        com_bad = 'Денег нет, держись'
        com_better = 'Денег нет, держись: твой долг - N руб/USD/Euro {cash_remained}{money}'
        com_ost = f'Сегодня осталось {cash_remained} {money}'
        com_not_in = 'Валюта {money} не рассматривается в программе'

        if cash_remained == 0:
            return com_bad

        if money not in money_many:
            return com_not_in

        name, rate = money_many[money]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            return com_ost
        else:
            return com_better

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)


# дата в параметрах не указана, так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

#print(f'1. week stst {cash_calculator.get_week_stats()}') 1. week stst 445
print(f'2. {cash_calculator.get_today_cash_remained()}')
#print(f'3. limit blnc for today {cash_calculator.get_today_limit_balance()}') 3. limit blnc for today 555

calories_calculator = CaloriesCalculator(3000)
calories_calculator.add_record(Record(amount=1186,comment='Кусок тортика. И ещё один.', date='24.02.2019'))
calories_calculator.add_record(Record(amount=84, comment='Йогурт.', date='23.02.2019'))
calories_calculator.add_record(Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019'))


#print(f'5.{calories_calculator.get_calories_remained()}') 5.Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 3000 кКал
# должно напечататься
# На сегодня осталось 555 руб
