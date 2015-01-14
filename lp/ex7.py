
# -*- coding: utf-8 -*-

number = 10
second_number = 0
first_list = [1, 2]
second_list = [1, 2, 3]

if number > 5:
    print '1'

if first_list:
    print '2'

if len(second_list) == 3:
    print '3'

if len(first_list) + len(second_list) == 5:
    print '4'

if first_list and first_list[0] == 1:
    print '5'

if not second_number:
    print '6'
