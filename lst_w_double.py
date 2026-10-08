def fusion(*lst):
    view = set ()
    result = list ()
    
    for lt in lst :
        for el in lt :
            if el not in view :
                result.append (el)
                view.add (el)
    
    return result
    
lst1 = ["Pomme", "Banane", "Grenade", "Ananas"]
lst2 = ["Avocat", "Pomme", "Goyave", "Pêche", "Banane"]

lst3 = fusion(lst1, lst2)
print(lst3)