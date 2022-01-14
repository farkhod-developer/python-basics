from random import randint
ism = (input('Iltimos ismingizni kiriting: \n>>> '))
togri = 0
hato = 0 
for i in range(1,6):
    a = randint(1,50)
    b = randint(1,50)
    d = randint(1,4)
    if d == 1:
        c = int(input(f'{a} * {b} = '))       #Hisoblash uchun RANDOM orqali ihtiyoriy son chiqarib beradi. "KO'PAYTIRISH"
        if c == (a*b):
            togri += 1
        else:
            hato += 1
    elif d == 2:
        c = int(input(f'{a} // {b} = '))       #Hisoblash uchun RANDOM orqali ihtiyoriy son chiqarib beradi. "BO'LISH"
        if c == (a//b):
            togri += 1
        else:
            hato += 1
    elif d == 3:
        c = int(input(f'{a} - {b} = '))       #Hisoblash uchun RANDOM orqali ihtiyoriy son chiqarib beradi. "AYIRISH"
        if c == (a-b):
            togri += 1
        else:
            hato += 1
    elif d == 4:
        c = int(input(f'{a} + {b} = '))       #Hisoblash uchun RANDOM orqali ihtiyoriy son chiqarib beradi. "QO'SHISH"
        if c == (a+b):
            togri += 1
        else:
            hato += 1                        
print (f" Hurmatli {ism.title()} togri javobingiz {togri} ta \n Hato javobingiz {hato} ta")
