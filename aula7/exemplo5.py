import os
os.system('cls')

num = int(input('Digite um numero decimal: '))

binario = ''

while num > 0:
    r = num%2
    binario = str(r) + binario 
    num = num//2

print(binario)