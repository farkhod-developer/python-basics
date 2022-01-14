# a = int(input('son kiriting: '))
# b = float(input('son kiriting: '))
# print((a > b), 'print1')
# print((a < b), 'print2')
# print((a == b), 'print3')     #mantiqiy amallar
# print((a >= b), 'print4')
# print((a <= b), 'print5')
# print((a != b), 'print6')

# a = int(input('sonni kiriting'))
# if a==0:
#     print('juft ham, toq ham emas')           #sonlarning toq yoki juftligini aniqlash.
# elif a%2==0:
#     print('juft son')
# else:
#     print('toq son')

# a = int(input('4 xonali son kiriting: '))
# if a>999 and a<10000:
#     print('4 xonali son')
# elif a>9999 and a<100000:                     #4 xonali sonlar
#     print('5xonali son')
# else:
#     print('4 xonali son emas!')

# a = int(input('1-son: '))
# b = int(input('2-son: '))
# c = int(input('3-son: '))
# if a>b:
#     b=0
#     print(b)
# else:
#     print(b)

# if a**2 - b**2 ==c**2:
#     print(a*b*c)
# else:
#     print(a+b+c)

# if a>0:
#     print(a*10)
# elif a==0:
#     print('ishora yuq')
# else:
#     print(a)


dostlar = []
print('5 ta eng yaqin dostingiz kim')
for i in range(5):
    dostlar.append(input(f" {i+1}- do'stingizni kiriting..."))
print(dostlar)
