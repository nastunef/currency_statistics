from datetime import datetime
import requests
from dateutil import parser
from statistic.models import Statistics


class ReadJson(object):
    def __init__(self):
        self.url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        self.js = None
        self.month = datetime.now().month - 1
        self.year = datetime.now().year
        if self.month == 0:
            self.month = 12
            self.year -= 1

    def __call__(self):
        while True:
            # читаем файл
            self.js = self.get_json()
            # смотрим дату данных
            js_date = self.get_date().date()
            # если нужный месяц и год
            if js_date.month == self.month and js_date.year == self.year:
                # добавление в базу
                st = Statistics(data=js_date, usd=self.get_valuta_value('USD'),
                                eur=self.get_valuta_value('EUR'),
                                jpy=self.get_valuta_value('JPY'),
                                cny=self.get_valuta_value('CNY')
                                )
                st.save()
            # если еще не дошли до него
            elif js_date.month < self.month and js_date.year <= self.year:
                break
            # получаем следующий url файла
            self.url = 'https:' + self.js['PreviousURL']

    def get_json(self):
        return requests.get(self.url).json()

    def get_valuta_value(self, name_valuta):
        return self.js['Valute'][name_valuta]['Value']

    def get_date(self):
        return parser.parse(self.js['Date'])
