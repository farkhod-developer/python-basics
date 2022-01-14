# s = []
# a = int(input('son kiriting: '))
# # for i in range(1,a+1):
#     b = input(f'{i} oila azolarizi kiriting: ')       #list orqali malumotlarni qo'shish va o'chrish.
#     s.append(b)
# print(s)    
# d = input('qaysini uchirish kerak: ')    
# s.remove(d)
# print(s)  


# s = []
# k = 0
# a = int(input('son kiriting: '))
# for i in range(1,a+1):
#     b = int(input(f'{i} son: '))    
#     while b <= 0:
#         print('Nol va noldan kichik son kiritish mumkin emas')  #nol va noldan kichigini qabul qilmaydi.
#         b = int(input(f'{i} son: ')) 
#     s.append(b)
#     print(s)
# for j in s:  
#     k = k+j
# print(k)
 

# s = []
# k = 0
# a = int(input('son kiriting: '))
# for i in range(1,a+1):
#     b = int(input(f'{i} son: '))    
#     while b <= 0:
#         print('Nol va noldan kichik son kiritish mumkin emas')  #nol va noldan kichigini qabul qilmaydi.
#         b = int(input(f'{i} son: ')) 
#     s.append(b)
#     print(s)
# for j in s:  
#     k = k+j
# print(k)

# a = ('ali, vali, soli')
# b = tuple (sorted(a))         #TUPLE 
# print(type(b))





n = int(input('n sonini kiriting:'))
s = 0
for i in range(n):
    s+=i
    print(s)