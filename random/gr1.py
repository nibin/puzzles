#!/usr/bin/python
# -*- coding: utf-8 -*-
#finding longest palindrome

def process_me(a,i,j):
  while(True):
    i+=1
    j-=1
    if(j<i):
      return True
    if(a[i]==a[j]):
      pass
    else:
      return False

a = """FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibe
rtyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhe
therthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftz
hatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthat
thatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewe
cannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfar
aboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcannever
forgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughthereh
avethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonor
eddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethat
thesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmento
fthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"""
l = []
for i in range(0,len(a)):
  for j in range(i+2,len(a)):
    if(a[i]==a[j]):
      b = process_me(a,i,j)
      if(b == True):
	l.append(a[i:j+1])
    
print l



    
    