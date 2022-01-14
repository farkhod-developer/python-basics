# ruyxatlar = ['gosht', 'gurunch', 'sabzi', 'piyoz', 'yog']
# ruyxatlar.append('un')                                        #ro'yxatga yangi matn qo'shish mumkin.
# # # # ruyxatlar.insert(2, 'kartoshka, pomidor')               #ro'yxatni index ko'rsatilgan joyga qo'shib beradi.
# # # # ruyxatlar.remove('yog')                                 #remove ichidagi ro'yxatni o'chirib tashlaydi.
# # del ruyxatlar[3]                                            #ro'yxatni index ko'rsatilgan joyini o'chiradi
# print(ruyxatlar)

# bozorlik = ['yog', 'un', 'piyoz', 'banan']
# bozorlik1 = ['yog', 'un', 'piyoz', 'banan']
# # mahsulot = bozorlik.pop(3)                        #.pop() funcsiyasi index ko'rsatilgan joydan ro'yxatni sug'irib oladi
# bozorlik.sort()                                   #.sort() metodi ro'yxatni alfabit bo'yicha taklab beradi
# # bozorlik1.sort(reverse = True)                    ro'yxatni teskarisiga taklab beradi
# # print('Men ' +mahsulot+ ' sotib oldim')           
# # print('Olinmagan mahsulotlar: ', bozorlik)
# print(bozorlik,  bozorlik1)

# mehmonlar = ['Ali', 'Vali', 'soli', 'Husan', 'Muxsin']
# for mehmon in mehmonlar:
#     print('Sizni ko\'rganimdan hursandman ', mehmon)         #For tsikli ustida amallar
#     print('Yana kelib turing ', mehmon )

# mehmonlar = ['Ali', 'Vali', 'soli', 'Husan', 'Muxsin']
# for mehmon in mehmonlar:
#     print(f'Hurmatli {mehmon}, sizni 30-iyun kuni bo\'ladigon oshga taklif etamiz')       #For tsiklini "f" string bilan chop etish.
#     print('Hurmat bilan, Polonchiyevlar oilasi \n')

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f'{son} ning kvadrati {son**2} ga teng')    #For tsiklida matematik amallar

# dostlar = []
# print('5 ta eng yaqin do\'stingiz kim? ')             #For tsiklida input() orqali ma'lumot kiritamiz.
# for dost in range(5):
#     dostlar.append(input(f'{dost+1} -do`stingizni ismini kiriting: '))
# print(dostlar)
