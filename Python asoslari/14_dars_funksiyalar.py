# def musbat_son(a,b):

#     if a>0:
#         return f'{a} ** {b} = {a**b} ga teng!'
#     # elif a==0:
#     #     print('siz nolga teng qiymat kirittingiz iltimos noldan katta son kiriting: ')
#     #     k = int(input('son kiriting: '))
#     # else:
#     #     print('kechirasz siz manfiy son kirittingiz')

# k = int(input('a son kiriting: '))
# x = int(input('b son kiriting: '))
# print(musbat_son(k,x))



# son = int(input('son kiriting: ')) 
# def ixtiyoriy_ism(son):
#     list = []
#     for i in range(1,son+1):
#         s = input(f'oila azoyingizni kiriting: ')     #nech marta son kiritsa oila a'zolarini shuncha so'raydi.
#         list.append(s)
#     return list
# print(ixtiyoriy_ism(son))



# def son(a):
#     k = 0

#     for i in a:
#         if i>0:
#             k += i
#     return k
# list = [1,5,7,-5,-3,6]
# print(son(list))


# def turi(son):
#     mus = []
#     man = []
#     mantiq = []
#     string = []
#     f= []
#     for i in son:
#         if type(i) == int:
#             if i>0:
#                 man.append(i)
#             elif i<0:
#                 mus.append(i)             #listlarga aloxida qilib chiqarib beradi
#         elif type(i) == bool:
#             mantiq.append(i)
#         elif type(i) == float:
#             f.append(i)
#         else:
#             string.append(i)
#     return man, mus, mantiq, string
# l = [2, 5, 4, -5, -9, 4, -7, True, False, 'ali', 'vali', 'soli']
# print(turi(l))


# def sonlar(a):
#     s = []
#     for i in a:
#         if i not in s:
#             s.append(i)          #bir xillik sonlarni olib tashlaydi.
#     return s
# l = [1,1,2,2,3,3,4]
# print(sonlar(l))


# def sonlar(a):
#     s = []
#     x = 0
#     for i in a:
#         if i not in s:
#             s.append(i)          #bir xillik sonlarni olib tashlaydi.
#             if i % 2 == 0:
#                 x = i ** 2
            
        
#     return s
    
# l = [1,1,2,2,3,3,4]
# print(sonlar(l))




# def turi(son):
#     katta = []
#     kichik = []
#     raqam = []
#     belgi = []
    
#     for i in son:
#         if type(i) == str:
#             if i == i.upper():
#                 katta.append(i)
#             elif i == i.lower():
#                 kichik.append(i)             #listlarga aloxida qilib chiqarib beradi
#             elif type(i) == int:
#                 raqam.append(i)
#         else:
#             belgi.append(i)
#     return katta, kichik, raqam, belgi
# l = [ 2,8,47,3, 'ALI', 'VALI', 'SOLI', 'ali', 'vali', 'soli']
# print(turi(l))