
# -*- coding: utf-8 -*-

def list_benefits():
    return ("More organized code",
            "More readable code",
            "Easier code reuse",
            "Allowing programmers to share and connect code together")

def build_sentence(info):
    return info + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print build_sentence(benefit)

name_the_benefits_of_functions()
