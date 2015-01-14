
# -*- coding: utf-8 -*-

import re

find = [word for word in dir(re) if "find" in word]
find.sort()
print find
