soat1 = int(input('1-soat: '))
minut1 = int(input('1-minut: '))
secund1 = int(input('1-secund: '))

soat2 = int(input('2-soat: '))
minut2 = int(input('2-minut: '))
secund2 = int(input('2-secund: '))

secund = (soat2 - soat1) * 3600 + (minut2 - minut1) * 60 + (secund2 - secund1)
print(f'secund: ', secund)