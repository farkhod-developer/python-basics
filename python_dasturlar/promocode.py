from random import randint
kodlar = [132, 134, 138, 140]# bu listdagi kodlar takrorlanmaydi.
yangi_kod = randint(130, 140) # promokodlar oraliq soni.


while yangi_kod in kodlar:
    yangi_kod = randint(130, 140)

print(yangi_kod)
