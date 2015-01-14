
# -*- coding: utf-8 -*-

def type_check(correct_type):
    def compare_type(old_func):
        def new_func(arg):
            if isinstance(arg, correct_type):
                return old_func(arg)
            else:
                print "Bad Type"
        return new_func
    return compare_type

@type_check(int)
def times2(num):
    return num*2

print times2(2)
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print first_letter('Hello World')
first_letter(['Not', 'A', 'String'])
