# class gogo(object):
#     def __init__(self, path = ''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return gogo('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#         # return tem
#
#     __repr__ = __str__
#
#     def __call__(self, path = ''):
#         return gogo('%s/%s' % (self._path, path))
#
# print(gogo().a('3').b.c.d.e)


# -*- coding: utf-8 -*-

from enum import Enum
import unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
