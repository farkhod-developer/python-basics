# k = int(input('n sonini kiriting: '))
# n = int(input('k sonini kiriting: '))
# s = 0
# if k<n:
#     for i in range(n-1,k,-1):
#         s = s+1
#         print(i,s)

# som = float(input('1 kg konfet narxi: '))
# d = 1
# for i in range(1,11):                            #1kg konfetning gramini summasini hisoblab beradi
#     d = som*i
#     print(f'{i/100} g konfet narxi {i*som/100}')


# a = int(input('a son kiriting: '))
# b = int(input('b son kiriting: '))
# s = 0
# if a<b:
#     for i in range(b,a-1,-1):
#         s = s+1
#         print(i)
#     print(s)

# n = int(input('n sonini kiriting: '))
# k = 1
# s = 1
# for i in range(2,n+1):
#     s+=k/i
#     print(s)


# n = int(input('n sonini kiriting: '))

# if n > 0:
#      s = 0
#     for i in range(n, (n+n)+1):
#          i = i ** 2
#          s += i
# print(s)

# a = int(input('a sonini kiriting: '))
# b = int(input('b sonini kiriting: '))
# s = 1
# if a<b:
#     for i in range(a,b+1):
#         s = s*i
#         # print(i)
#         print(s*(i**2))

# n = int(input('n sonini kiriting: '))
# d = 1
# k = 1
# if n>0:
#     for i in range(1,n+1):
#         k *= d+(i/10)
#         print(k)


n = int(input(' n sonini kiriting: '))
d = 0
s = 0
for i in range(11,n+1,2):
    s = s+(i/10)
for j in range(12, n+1, 2):
    d = d+(j/10)
print(f'{s-d}')