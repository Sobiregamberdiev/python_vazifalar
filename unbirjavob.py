# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:30:58 2025

@author: hp victus
"""
# son=int(input('juft son kirgizing.>>>'))
# if son % 2== 0:
#     print('rahmat')
# else:
#     print('bu son juft emas!')
    
    
# yosh=int(input('yoshingiz nechida?'))
# if yosh<=4 or yosh>60:
#     price=0
#     print(f'sizga kirish {price} sum!')
# elif yosh<=18:
#     price=10000
#     print(f'sizga kirish {price} sum!')
# elif yosh>=18:
#     price=20000
#     print(f'sizga kirish {price} sum!')

# x=float(input('birinchi sonni kiriting>>>'))
# y=float(input('ikkinchi sonni kiriting>>>'))
# if x==y:
#     print(f'{x}={y}')
# elif x<y:
#     print(f'{x}<{y}')
# else:
#         print(f'{x}>{y}')

# mahsulotlar=['anor','olma','piyoz','bodring','tuz','shakar','non','sut','un','yog']
# savat=[]
# for n in range(5):
#     savat.append(input(f'savatga {n+1}-mahsulotni qushing!'))
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f'dukonimizda {mahsulot} bor!')
# else:
#     print(f'dukonimizda {mahsulot} yoq!')
    
# mahsulotlar=['anor','olma','piyoz','bodring','tuz','shakar','non','sut','un','yog']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# userz=['alisher','aziza','yasina','umar']
# login=input('yangi login tanlang:>>>')
# if login in userz:
#     print('login band yangi login tanlang!')
# else:
#     print(f"xush kelibsiz,{login.title()}!")
    
son=int(input('istalgan butun son kiriting:>>>'))
for n in range(2,11):
    if not (son%n):
        print(f'{son} soni {n} ga qoldiqsiz bulinadi!')
             
     

