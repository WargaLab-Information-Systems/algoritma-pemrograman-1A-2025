n = 5

for i in range(1, n + 1):
    for kn in range(1, i + 1):
        print(kn, end=' ')
        
    for spasi in range(2 * (n - i)):
        print('  ', end='')
    
    for kr in range(i, 0, -1):
        print(kr, end=' ')
    
    print()
