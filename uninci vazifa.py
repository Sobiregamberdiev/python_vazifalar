# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:07:50 2025

@author: hp victus
"""


# cars=['toyota','mazda','gm','lada','ford'] 
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#             print(car.title())

# cars=['toyota','mazda','gm','lada','ford'] 
# for car in cars:
#     if car != 'gm':
#         print(car.upper())
#     else:
#             print(car.title())
            
            
# login = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
# if login.lower() == 'admin': # Agar ism Aliga teng bo'lmasa ...
#     print(" xush kelibsiz  Admin, foydalanuvchilar ruyxatini kurasizmi? ") # quyidagi xabar chiqadi
# else:
#     print(f"assalomu aleykum {login.title()}")
    
x=float(input('birinchi sonni kiriting:'))
y=float(input('ikkinchi sonni kiriting:'))
if x==y: print(f'sonlar teng: {x}={y}')

son=float(input('istalgan son kiriting:'))
print('son manfiy') if son<0 else print('son musbat')
 
son= float(input('istalgan son kiriting:'))
print(son**(1/2)) if son >0 else print('musbat son kiriting')