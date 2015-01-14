
# -*- coding: utf-8 -*-

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(num) for num in numbers if num > 0]

print newlist
