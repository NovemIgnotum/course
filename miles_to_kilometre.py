ref_miles = 1.609
kilometer = int(input("Veuillez entrer une vitesse en km/h :"))
miles = kilometer/ref_miles
miles = round(miles, 2)
print(f'{kilometer} km/h = {miles} m/h')