# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:37:13 2025

@author: hp victus
"""

davlatlar=["AQSH","Mexiko","Turkiya","Uzbekistan","Misr","India"]
#print("Davlatlar Soni:",len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)
sonlar=list(range(120,1200,2))
#print(sonlar)
#print(sum(sonlar))
#print(max(sonlar)-min(sonlar))
#print(sonlar[:20])
#print(sonlar[-20:])
#print(sonlar[530:550])
taomlar=["osh","manti","norin","somsa","pizza"]
nonushta=taomlar[:]
#print(nonushta)
#print(taomlar)
nonushta.remove('norin')
nonushta.remove('osh')
nonushta.remove('pizza')
nonushta.append('manti')

#print(nonushta)
#print(taomlar)
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
lnonushta[0] = "qaymoq va non"