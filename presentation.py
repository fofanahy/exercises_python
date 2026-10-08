name = input("Votre nom ? ")
fastname = input("Votre prénom ? ")
age = int(input("Votre age ? "))

presentation = f"""
Je m'appelle {name.capitalize()} {fastname.capitalize()}, J'ai {age} ans.
"""

print(presentation)