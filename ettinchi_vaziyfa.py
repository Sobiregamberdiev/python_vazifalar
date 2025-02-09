# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:18:01 2025

@author: hp victus
"""

ismlar=["Abror", "Mahmud","Solih"]
dust = ismlar [0]
#aka = ismlar [-1]
print("Salom " + dust + " bugun choyxona ochiqmi?")
print(ismlar[-1]+ " choyxonaga boramizmi?" )

sonlar=[10,80,70,-20,5.5]
print(sonlar[1])

t_shaxslar=["Imom Buxoriy","Termiziy","Nasoiy"]
z_shaxslar=["Ilon Mask","Bil Gates","Margulan"]
imom= t_shaxslar.pop(0)
shaxs= z_shaxslar.pop(1)
#print("Men tarixiy shaxslardan "+imom+ " bilan \nsuhbat qilishni istar edim!")
#print("Zamonaviy shaxslardan esa "+shaxs+" bilan \nsuhbat qilishni istardim!")
friends=[]
friends.append("Karim")
friends.append("Eshmat")
friends.append("Toshmat")
friends.append("Anvar")
friends.remove("Toshmat")
#print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop())
print("Kelgan mehmonlar:\n", mehmonlar)