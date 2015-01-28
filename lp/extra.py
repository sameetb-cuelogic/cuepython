
# -*- coding: utf-8 -*-

# 1st
# def mk_class(**kwargs):
#     return type('MyClass', (object,), dict(**kwargs))

# my_class = mk_class(foo=2, bar="bar")
# print my_class

# my_object = my_class()
# print my_object
# print my_object.foo, my_object.bar

# 2nd
# class MyMeta(type):

#     def __new__(cls, name, bases, attrs):
#         print "__new__"
#         print cls
#         print name
#         print attrs
#         return super(MyMeta, cls).__new__(cls, name, bases, attrs)

#     def __init__(cls, name, bases, attrs):
#         print "__init__"
#         print cls
#         print name
#         print attrs
#         return super(MyMeta, cls).__init__(name, bases, attrs)

#     def __call__(cls, *args, **kwargs):
#         print "__call__"
#         print cls
#         print args
#         print kwargs
#         return super(MyMeta, cls).__call__(*args, **kwargs)


# class MyClass(object):
#     __metaclass__ = MyMeta

#     def __init__(self, param):
#         print param

#     def foo(self, param):
#         print

#     bar = "bar"

# 3rd
class BeanMeta(type):

    def __init__(cls, name, bases, attrs):
        super(BeanMeta, cls).__init__(name, bases, attrs)

        prop_list = {}

        for attr in attrs.keys():
            if (attr.startswith("set_") or
                    attr.startswith("get_")):
                prop_list.setdefault(attr[4:], {"set_": None, "get_": None})[attr[:4]] = getattr(cls, attr)

        for prop_name, props in prop_list.iteritems():
            setattr(cls, prop_name, property(props["get_"], props["set_"], None, None))


class TestBean(object):
    __metaclass__ = BeanMeta
    __prop1 = None
    __prop2 = None

    def get_prop1(self):
        print "get_prop1"
        return self.__prop1

    def set_prop1(self, value):
        print "set_prop1"
        self.__prop1 = value

    def get_prop2(self):
        print "get_prop2"
        return self.__prop2

    def set_prop2(self, value):
        print "set_prop2"
        self.__prop2 = value

#     prop = property(get_prop, set_prop, None, None)

# t = TestBean()
# t.prop1 = 10
# print "prop1:", t.prop1
# t.prop2 = 20
# print "prop2:", t.prop2
