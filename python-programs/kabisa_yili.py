kabisa = int(input('Yilni kiriting '))
if kabisa % 4 != 0:
     print(f'{kabisa}-yil kabisa yili emas!')
elif kabisa % 100 == 0:
    if kabisa % 400 == 0:
        print(f'{kabisa}-yil kabisa yili')
    else:
        print(f'{kabisa}-yil kabisa yili emas!')
else:
    print(f'{kabisa}-yil kabisa yili')
