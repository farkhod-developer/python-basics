sum = int(input("so'm: "))
tiyin = int(input("tiyin: "))
kg = int(input("Kg: "))

natija = kg * ((sum * 100) + tiyin)
print("so'm: ", natija // 100)
print("tiyin: ", natija % 100)