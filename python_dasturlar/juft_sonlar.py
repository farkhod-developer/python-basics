
n = int(input('n sonini kiriting: '))
k = 0
for son in range(2, n+1):
    k = son%2
    if k == 0:
        k += son
    else:
        continue
    
        
    print("yig'indi - ", k)