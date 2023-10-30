multiple = [1,2,3,4,5,6,7,8,9,10]
res_multiple = []

number = int(input("Chois un nombre :"))

for i in multiple:
    res = i * number
    res_multiple.append(res)

print(f'Voila les 10 premières multiplacation de {number} \n {res_multiple}')
