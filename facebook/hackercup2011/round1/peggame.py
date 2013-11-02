#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re 

a_txt = '''5
5 4 0 1 2 2
3 4 1 1 1 0
3 3 1 2 1 1 1 0
3 4 0 2 1 0 1 1
3 4 0 1 1 1
'''


#f = open(sys.argv[1],'r')
#content =  f.read().splitlines()
content = a_txt.splitlines()
n = int(content[0])
results = {}
line_no = 0
test_case = []
#f.close()

for i in range(0,n):
  line_no+=1
  d = {}
  temp_list = re.split('\s+',content[line_no])
  r = int(temp_list[0])
  c = int(temp_list[1])
  k = int(temp_list[2])
  m = int(temp_list[3])
  pairs = []
  for j in range(0,m):
    pairs.append((int(temp_list[4+ (2 * j)]),int(temp_list[4+ (2*j +1) ])))
  
  d['R'] = r
  d['C'] = c
  d['K'] = k
  d['M'] = m
  d['PAIRS'] = pairs
  
  test_case.append(d)

#for jj in range(0,len(test_case)):
  #print test_case[jj]

def debug_print(a_list):
  for i in range(0,len(a_list)):    
    for j in range(0,len(a_list[i])):
      print "%s " % str(a_list[i][j]),
    print


def did_hit_target(row_matrix,row_level,col_level,d):
  target_coordinate = set( [ ( d['R'], d['K']*2+1 ) ] )
  cand_coordinate = (row_level, col_level)
  if cand_coordinate in target_coordinate:
    #success
    return 1
  if(row_level >= d['R']):
    #Failed
    return -1  
  return 0

def resolve_coordinate(row_level,col_level):
  r = row_level
  c = col_level
  if(row_level % 2 == 0):
    c = col_level/2
  else:
    c = (col_level-1)/2
  return (r,c)

def is_far_left_or_right(row_matrix,row_level,col_level,colsize):
  if(row_level % 2 == 0):
    if(col_level == (colsize*2 -2)):
      #bounce to left
      return -1
    elif(col_level == 0):
      #bounce to right
      return 1
    else:
      #continue
      return 0
  else:
    if(col_level == (colsize-1)*2 -1):
      return -1
    elif(col_level == 1):
      return 1
    else:
      return 0

def coordinate_to_abs(tup):
  r , c = tup
  row_level = r
  col_level = c
  if(r % 2 == 0):
    col_level = c * 2
  else:
    col_level = (c * 2) +1
  return (row_level,col_level)

def bounce_right_or_left(paths_from_d_point,path):
  for branch in paths_from_d_point['BRANCH']:
    if path == branch:
      return 1
  return -1



for i in range(0,n):
  print
  print "Game#%d" % i
  result_line = []
  row_matrix = []
  col_matrix = [ch for ch in ['x','.']]
  d = test_case[i]
  
  '''
  for j in range(0,d['R']):
    #rows
    
    if(j % 2 == 0):
      lcol_matrix = col_matrix * (d['C'] - 1) + ['x']
      row_matrix.append(lcol_matrix)
    else:
      lcol_matrix = ['-'] + (col_matrix * (d['C'] - 2)) + ['x','-']
      row_matrix.append(lcol_matrix)
  
  for k in range(0,d['M']):
    pair = d['PAIRS'][k]
    if(pair[0] % 2 == 0):
      row_matrix[pair[0]][pair[1]*2] = '.'
    else:
      row_matrix[pair[0]][(pair[1]*2)+1] = '.'
  '''
  target_column = d['K']
  
  res_dict = {}
  all_paths = { }
  
  #debug_print(row_matrix)
  
  for d_point_column in range(0,d['C']-1):
    #walk-path and record
    paths_from_d_point = { }
    paths_from_d_point['SUCCESS'] = []
    paths_from_d_point['FAILED'] = []  
    paths_from_d_point['BRANCH'] = []  
    all_paths[d_point_column] = paths_from_d_point
    
    row_level = 0
    col_level = (d_point_column*2)+1
    path = []
    
    while True:
      
      s = did_hit_target(row_matrix,row_level,col_level,d)
      if(s > 0):
	#success
	paths_from_d_point['SUCCESS'].append(path)
	#print " SUCCESS(%d) " % (d_point_column),
	#print path
	l = len(paths_from_d_point['BRANCH'])
	if(l > 0):
	  path = paths_from_d_point['BRANCH'][l-1]
	  row_level, col_level = coordinate_to_abs(path.pop())
	else:
	  #no more branches to proceed
	  break
      elif(s < 0):
	#failed
	paths_from_d_point['FAILED'].append(path)
	#print " FAILED(%d) " % (d_point_column),
	#print path
	l = len(paths_from_d_point['BRANCH'])
	if(l > 0):
	  path = paths_from_d_point['BRANCH'][l-1]
	  row_level, col_level = coordinate_to_abs(path.pop())	  
	else:
	  #no more branches to proceed
	  break
	
      
      
      if(row_matrix[row_level][col_level] == '.'):
	#its a space, go down
	#path.append(resolve_coordinate(row_level,col_level))
	row_level +=1
      elif(row_matrix[row_level][col_level] == 'x'):
	#hit a peg
	val = is_far_left_or_right(row_matrix,row_level,col_level,d['C'])
	if(val > 0):
	  #bounce to right
	  path.append(resolve_coordinate(row_level,col_level))
	  row_level += 1
	  col_level += 1
	elif(val < 0):
	  #bounce to left
	  path.append(resolve_coordinate(row_level,col_level))
	  row_level += 1
	  col_level -= 1
	else:
	  path.append(resolve_coordinate(row_level,col_level))
	  v = bounce_right_or_left(paths_from_d_point,path)
	  if(v < 0):
	    #bounce to left
	    # I will by default bounce to left and record the path for
	    # future forking from here
	    #path.append(resolve_coordinate(row_level,col_level))
	    c_path = path[:]
	    paths_from_d_point['BRANCH'].append(c_path)
	    row_level += 1
	    col_level -= 1
	  elif(v > 0):
	    #path.append(resolve_coordinate(row_level,col_level))
	    # I have taken the other path
	    paths_from_d_point['BRANCH'].remove(path)
	    row_level += 1
	    col_level += 1
	  else:
	    print "Uncertain path at ",
	    print resolve_coordinate(row_level,col_level)
	    debug_print(row_matrix)
	    
    s_count = len(paths_from_d_point['SUCCESS'])
    f_count = len(paths_from_d_point['FAILED'])
    
    res_dict[d_point_column] = float((s_count*1.0)/(s_count+f_count))
  results[i] = res_dict 
	    
	
	    
  
  #debug_print(row_matrix)


print "=======Statistics=========="
for i in results.keys():
  print "(Game#%d) = > " % (i),
  print results[i]


print "=====Results=========="
print
max_in_line = []
for i in range(0,n):
  mx = max(results[i].values())
  for j in range(0, (test_case[i]['C'])-1):
    if(results[i][j] == mx):
      max_in_line.append("%d %0.6f" % (j,mx))
      break

for mm in max_in_line:
  print mm
  
print






