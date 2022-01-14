# def ixtiyoriy_nom(a,b):
#     '''bu funksiya eng kotta sonni ekranga chiqarib beradi!'''
#     if a>b:
#         print(a)
#     elif a==b:
#         print('a va b sonlar teng! ')
#     else:
#         print('b kichkina son')
# k = int(input('a sonini kiriting: '))
# x = int(input('b sonini kiriting: '))
# ixtiyoriy_nom(k,x)


# def ixtiyoriy_nom(a):
#     '''bu funksiya musbat yoki manfiyligini aniqlab beradi!'''
#     if a>0:
#         print(f' {a} siz musbat son kiritdingiz')
#     elif a==0:
#         print(f'{a}: nolga teng')
#     else:
#         print(f' {a} siz manfiy son kiritdingiz')
# k = int(input('a sonini kiriting: '))
# ixtiyoriy_nom(k)



def ixtiyoriy_nom(a,b):
    '''bu funksiya ikkalasini ham manfiy musbatini aniqlab beradi!'''
    if a>0 and b>0:
        if a>b:
            print(f'{a} son musbat {b} son musbat \n{a} son kotta {b} son kichik')
        if a>b:
            print(f'{a} son musbat {b} son manfiy \n{a} son kotta {b} son kichik')      #tayyor emas!
    elif a==b:
        print(f' {a} son  va {b} sonlar teng! ')
    else:
        if a<-1 and b<-1:
            print(f' {a} son manfiy {b} son manfiy \n{a} son kichik {b} son kotta')
k = int(input('a sonini kiriting: '))
x = int(input('b sonini kiriting: '))
ixtiyoriy_nom(k,x)