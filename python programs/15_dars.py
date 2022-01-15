# def turi(son):
#     katta = 0
#     kichik = 0
#     raqam = 0
#     belgi = 0 
#     for i in son:
#         if i.isnumeric():
#             raqam+=1
#         elif i in '!@#$%^&*()_+':
#             belgi+=1
#         elif i == i.upper():            #raqamlar, belgilar, katta va kichik so'zlarni sonini aniqlab beradi.
#             katta+=1
#         elif i == i.lower():
#             kichik+=1                
#     return f'katta harflar: {katta} ta, kichik harflar: {kichik} ta, raqamlar: {raqam} ta, belgilar: {belgi} ta'
# print(turi('FRYGsdg23454!@#$%'))


# def nom(**kwargs):
#     for k in kwargs:
#         print(kwargs[k])          #kwargs ustida amallar
# nom(a=5)


# a = lambda x: x*x         #LAMBDA sintaksisi
# print(a(6))

# def b(x):
#     return lambda x: x**y
# kvadrat = b(2)
# print(kvadrat(2))
# print(kvadrat(3))
# print(kvadrat(4))
# kub = b(3)
# print(kub(2))
# print(kub(3))
# print(kub(4))