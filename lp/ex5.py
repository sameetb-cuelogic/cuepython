
# -*- coding: utf-8 -*-

data = ("John", "Doe", 53.4444)
format_string = "Hello %s %s. Your current balance is %.2f$"

print format_string % (data[0], data[1], data[2])
