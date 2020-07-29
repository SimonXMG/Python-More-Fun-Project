from datetime import datetime
t = datetime.today()
print ('Today is',datetime.strftime(t,'%m/%d/%Y'))
en = input('Give the name of an event: ')
d = input('Give the date of an event: ')
e = datetime.strptime(d,'%m/%d/%Y')
if t < e:
    days = str(e - t).split(',')[0]
    print('It is %s until %s' % (days, en))
else:
    days = str(t - e).split(',')[0]
    print('It is %s since %s' % (days, en))


