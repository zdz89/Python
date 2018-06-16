# -*- coding: cp1250 -*-
months = {'sty':1,'lut':2,'mar':3,
          'kwi':4,'maj':5,'cze':6,
          'lip':7,'sie':8,'wrz':9,
          'paz':10,'lis':11,'gru':12}

first = input('Podaj 1. miesiąc (3 pierwsze litery): ')
second = input('Podaj 2. miesiąc (3 pierwsze litery): ')

if months.get(first) == months.get(second):
    print(12)
elif months.get(second) < months.get(first):
    print(months.get(second) - months.get(first) + 12)
else:
    print(months.get(second) - months.get(first))
