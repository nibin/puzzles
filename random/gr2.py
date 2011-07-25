#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
#
import sys

def calculate_fib(fib,a):
  fib[0] = 0
  fib[1] = 1
  pos_a = 0;
  pos_b = 1
  while(True):
    fib[pos_b+1] = fib[pos_a] + fib[pos_b]
    if(a<=fib[pos_b+1]):
      print "fib[pos_b+1] %d" % fib[pos_b+1]
      print "fib[pos_b] %d" % fib[pos_b]
      break
    else:
      pos_a = pos_b
      pos_b+=1
    

def calculate_prime_divsor(a):
  l = []
  temp = a
  i=2
  while True:
    if(temp==1):
      break
    if(temp%i==0):
      l.append(i)
      temp=temp/i
      i=2
    else:
      i+=1
  print l
  k=1
  for i in range(0,len(l)):
    k=k*l[i]
  print "Computed: %d" % k
  s = set(l)
  
  print s
      
   
  

#a = int(sys.argv[1])
#fib={}
#calculate_fib(fib,a)
a = 317812
calculate_prime_divsor(a)



