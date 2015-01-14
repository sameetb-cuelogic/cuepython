
# -*- coding: utf-8 -*-

from functools import partial

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

partial_func = partial(func, 10, 10, 10)

print partial_func(-30)
