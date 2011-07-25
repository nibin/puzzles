#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

MAX_X = 2147483647
N = 100


f = open('suite_pz1.txt','w')
f.write(str(N) + '\n')
for i in range(0,N):
  f.write(str(random.randrange(MAX_X)) + '\n')

f.close()
