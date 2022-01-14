son = input('Ixtiyoriy butun son kiriting: ')
while not son.isdigit():
    print('Siz harf yoki belgilardan foydalandingiz !')
    son = input('Iltimos faqat butun son kiriting: ')
print(f'Siz kiritgan son <<{son}>>')