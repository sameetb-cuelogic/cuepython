
# -*- coding: utf-8 -*-

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print "Count x_list:", len(x_list)
print "Count y_list:", len(y_list)
print "Count big_list:", len(big_list)

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print "x and y lists are okay"

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print "All correct"
