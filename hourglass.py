h = 7
mil = h//2

for i in range (h) :
    n, m = (2*abs(mil-i)+1, mil-abs(mil-i))
    print(" "*m + "*"*n)