import random

reponse_difficulty = input("Choissisez une difficulté \n 1 = Facile : Chiffre de 0 à 10 \n 2 = Moyen : Chiffre de 0 à 100 \n 3 = Difficle : Chiffre de 0 à 1000 \n Diificulté :")
difficulty = int(reponse_difficulty)

if difficulty == 1 :
    secret_number = random.randint(0,10)
elif difficulty == 2 :
    secret_number = random.randint(0,100)
elif difficulty == 3 :
    secret_number = random.randint(0,1000)

user_try = 1

reponse = input("Entrez un nombre :")

while secret_number != reponse:
    reponse_number = int(reponse)
    if secret_number == reponse_number :
        print(f'Bravo ! le nombre est bien {reponse}. Vous avez toruvez en {user_try} essaies. ')
        break
    elif secret_number > reponse_number :
        print("Le nombre est plus grand.")
        user_try +=1
        reponse = input("Entrez un nombre :")
    elif secret_number < reponse_number :
        print("Le nombre est plus petit.")
        user_try +=1
        reponse = input("Entrez un nombre :")

        
