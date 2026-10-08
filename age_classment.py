try:
    age = int(input("Entrez votre age : "))
    
    if 120 >= age >= 0 :
        com = "Senior" if age >= 65 else "Adulte" if age >= 30 else "Adolescent" if age >= 15 else "Enfant" if age >= 5 else "Bébé"
        print(f"Vous êtes un {com}.")
    
    else: 
        print("Âge invalide !")

except ValueError:
    print("Doit être un nombre !")