def range_copy(start: int = None, stop: int = None, step: int = 1):
    
    if (stop is None):
        stop = start
        start = 1
    
    temp = start
    while (step > 0 and temp <= stop - 1) or (step < 0 and temp - 1>= stop):
        yield temp
        temp += step

for i in range_copy(10):
    print(i)