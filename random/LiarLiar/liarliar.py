#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

accussers = {}
f = open(sys.argv[1],'r')
content = f.read().splitlines()
line_no = 0
n = int(content[line_no])

for i in range(0,n):
  line_no+=1
  accusser_line = re.split('\s+',content[line_no])
  names = []
  for j in range(0,int(accusser_line[1])):
    line_no+=1
    names.append(content[line_no].strip())
  accussers[accusser_line[0]] = names

f.close()
#print accussers

candidates = set(accussers.keys())

#Build Truth condition for the first member
lcandidate = accussers.keys()[0]
candidates.remove(lcandidate)
good_boys = set([lcandidate])
bad_boys = set(accussers.get(lcandidate))

#k=1
while((len(candidates)>0) and (len(good_boys)+len(bad_boys) != n)):
  #print "Iter %d" % k
  #k+=1
  for c in good_boys:
    if c in candidates:
      bad_boys = bad_boys.union(accussers.get(c))
      candidates.remove(c)
  for c in bad_boys:
    if c in candidates:
      good_boys = good_boys.union(accussers.get(c))
      candidates.remove(c)
  cand_dup = candidates.copy()
  for c in cand_dup:
    c_accu = accussers.get(c)
    for a in c_accu:
      if a in good_boys:
	bad_boys = bad_boys.union([c])
	good_boys = good_boys.union(c_accu)
	candidates.remove(c)
	break
      elif a in bad_boys:
	good_boys = good_boys.union([c])
	bad_boys = bad_boys.union(c_accu)
	candidates.remove(c)
	break

size_groups = [len(good_boys),len(bad_boys)]
#print "%d %d" % ((size_groups[0],size_groups[1]) if (size_groups[0] >= size_groups[1]) else (size_groups[1],size_groups[0]))

if (size_groups[0] >= size_groups[1]):
  print "%d %d" % (size_groups[0],size_groups[1])
else:
  print "%d %d" % (size_groups[1],size_groups[0])
