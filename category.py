from collections import defaultdict

def classify(elements):
    gp = defaultdict(list)
    
    for el in elements :
        if isinstance(el, tuple):
            name, category = el
            gp[category].append(name)
    return gp

l = [("Aj", "Alpha"), ("Ax", "Alpha"), ("Bs", "Beta"), ("Bn", "Beta")]
print (classify(l))