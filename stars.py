h = 11
mil = h//2

for i in range (1, h+1):
    n, m = (2*i-1, mil-i+1) if i <= mil else (2*h-2*i+1, i-mil-1)
    print(" "*m + "*"*n)