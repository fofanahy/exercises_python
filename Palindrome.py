word = input("Entrez le mot : ").lower ()
is_pal = True if word == word[::-1] else False
if is_pal : print("C'est un palyndrome !")
else : print("N'est pas un palyndrome !")