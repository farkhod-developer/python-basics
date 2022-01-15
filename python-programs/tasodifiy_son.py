from random import randint

son1 = randint(1,20)
son2 = randint(1,20)
son3 = randint(1,20)
son4 = randint(1,20)

natija = int(input(f'{son1} + {son2} - {son3} * {son4} = '))

if natija == (son1 + son2 - son3 * son4):
    print('To`g`ri')
else:
    print('Xato!')