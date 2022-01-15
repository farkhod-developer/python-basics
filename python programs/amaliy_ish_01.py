# from uuid import uuid4
# '''uuid import uuid4 - bu method yordamida 
#     doimiy takrorlanmas ID raqam qaytaradi!'''
# class Avto:
#     '''Avtomobil klassi'''
#     __num_avto = 0
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#         '''[Avto.__num_avto += 1] - Avtomobilni sotib 
#         olinganlar sonini hisoblab boradi'''
    
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id

#     def add_km(self,km):
#         '''Mashinaning km ga yana km qushish'''
#         if km >= 0:
#             self.__km += km
#         else:
#             print('Mashina km ni kamaytirish mumkin emas')


cars = ['Malibu', 'Lacetti', 'Tahua', 'Gentra', 'Lada_Granta']
# model = cars.pop(1)
# cars.append('Tayotta')
# del cars[2]
# # print(model)
# print(cars)

cars.insert(len(cars),Tesla)
print(cars)