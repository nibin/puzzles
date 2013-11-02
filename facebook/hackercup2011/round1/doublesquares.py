# -*- coding: utf-8 -*-
#/usr/bin/python

import math
import sys

f = open(sys.argv[1],'r')
numbers =  f.read().splitlines()
n = int(numbers[0])
results = []
line_no = 0

def calc_perfect_squares(a,b,n):
  if(pow(a,2)+pow(b,2) == n):
    return True
  else:
    return False

def extract_and_check_ps(a,n):
  temp = n - pow(a,2)
  if math.sqrt(temp) == int(math.sqrt(temp)):
    return True
  else:
    return False

for i in range(0,n):
  line_no+=1
  _k = {}
  cand_number = int(numbers[line_no])
  upper_bound = int(math.sqrt(cand_number))
  lower_bound = int(math.sqrt(int(cand_number - int(upper_bound))))
  for j in range(upper_bound, int(math.sqrt(int(cand_number/2))),-1):
    temp = cand_number - pow(j,2)
    temp_sqrt = math.sqrt(temp)
    if temp_sqrt == int(temp_sqrt):
      if(not _k.has_key(max(j,int(temp_sqrt))) and not min(j,int(temp_sqrt)) in set(_k.values())):
	_k[max(j,int(temp_sqrt))] = min(j,int(temp_sqrt))
  
  #what about to the power 4 ?
  # 0 is a ds and count as 1--weird
  #upper_bound_sqrt = math.sqrt(upper_bound)
  #if upper_bound_sqrt == int(upper_bound_sqrt):
   # _k[int(upper_bound_sqrt)] = int(upper_bound_sqrt)
    
  results.append(len(_k))
  print "For %d - " % cand_number,
  print _k
  
  
for i in results:
  print i


