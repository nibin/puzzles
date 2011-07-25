#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

'''1
5 jibw ji jp bw jibw
'''


f = open(sys.argv[1],'r')
content =  f.read().splitlines()
#content = a_txt.splitlines()
n = int(content[0])
results = []
line_no = 0
word_line = {}

for i in range(0,n):
  line_no+=1
  temp_list = re.split('\s+',content[line_no])
  word_line[line_no] = sorted(temp_list[1:])
f.close()


def compare_words(a,b):
  max_size = len(a)
  if(max_size < len(b)):
    max_size = len(b)
  for i in range(0,max_size):
    if(i<=(len(a)-1) and i<=(len(b)-1)):
      if(a[i] > b[i]):
	return 1
      elif(a[i] < b[i]):
	return -1
      else:
	continue
    elif(i>(len(a)-1)):
      return 1
    elif(i>(len(b)-1)):
      return -1
    elif(len(a)==len(b) and i+1==max_size):
      return 0
    

for line in range(1,n+1):
  sorted_list = word_line[line]
  #size = len(sorted_list)
  #processed_word = []
  #max_size = max([len(it) for it in sorted_list])
  m = len(sorted_list)
  for i in range(0,m):
    for k in range(i+1,m):
      if(compare_words(sorted_list[i],sorted_list[k]) > 0):
	temp_sorted_list = sorted_list[:]
	sorted_list = temp_sorted_list[0:i] + [temp_sorted_list[k]] + temp_sorted_list[i+1:k] + [temp_sorted_list[i]] + temp_sorted_list[k+1:m]
  
  print ''.join(sorted_list)
	
    
	
      
      
      
      
  
  
  
