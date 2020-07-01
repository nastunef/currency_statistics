from datetime import datetime
import requests
from dateutil import parser
from statistic.models import *


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
            self.js = self.get_json()
            js_data = self.get_date().date()
            if js_data.month == self.month and js_data.year == self.year:
                # добавление в базу
                st = Statistics(data= js_data, usd= self.get_valuta_value('USD'),
                                eur= self.get_valuta_value('EUR'),
                                jpy= self.get_valuta_value('JPY'),
                                cny= self.get_valuta_value('CNY')
                                )
                st.save()
            elif js_data.month < self.month and js_data.year <= self.year:
                break
            # получаем следующий url файла
            self.url = 'https:' + self.js['PreviousURL']

    def get_json(self):
        return requests.get(self.url).json()

    def get_valuta_value(self, name_valuta):
        return self.js['Valute'][name_valuta]['Value']

    def get_date(self):
        return parser.parse(self.js['Date'])







