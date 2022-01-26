import pdb 
pdb.set_trace()



lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

maximos = [max(i) for i in lista]
print(maximos)


lista1 = [3, 4, 8, 5, 5, 22, 13, 111, 123, 121, 23]
def es_primo(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primos = list(filter(es_primo, lista1))

print(primos)