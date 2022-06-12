# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 10:32:08 2021

@author: saksh
"""

import random as rm
from datetime import datetime

rm.seed(datetime.now())
a = rm.randint(1, 2)

if (a==1):
    Head_or_tail = 'Head'
else:
    Head_or_tail = 'Tail'

print(Head_or_tail)