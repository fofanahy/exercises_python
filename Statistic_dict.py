def clc(dct: dict[str, (float, int)]):
    if not dct :
        return {"erreur": 0}
    
    vals = list(dct.values())
    if all(isinstance(val, (float, int)) for val in vals):
        return {
            "moyenne": sum(vals)/len(vals),
            "maximum": max(vals),
            "minimum": min(vals)
        }
    else :
        return {
            "type": {type(v).__name__ for v in vals},
            "Nombre": len(vals)
        }

dct = {"A": 1, "B": 2, "C": 2}
print(clc(dct))