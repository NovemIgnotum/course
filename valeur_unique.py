numbers = [8,7,11,7,2,10,5,8]
resutat = []

for i in numbers :
    if i not in resutat:
        resutat.append(i)

print(f'Liste avec doublon : {numbers}')
print(f'Liste sans doublon : {resutat}')

