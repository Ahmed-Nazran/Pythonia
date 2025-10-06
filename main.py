def find_outlier(ints):
    evens = [x for x in ints if x % 2 == 0]
    odds = [x for x in ints if x % 2 != 0]
    
    if len(evens) > len(odds): 
        return f"{odds[0]} (the only odd number)"
    else: 
        return f"{evens[0]} (the only even number)"
    
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
