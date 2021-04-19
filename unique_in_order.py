# Implement the function unique_in_order which takes as argument a sequence and returns a list of 
# items without any elements with the same value next to each other and preserving the original 
# order of elements.

def unique_in_order(iterable):
    i, y, final = "", ([]), ([])

    for x in iterable:
        y.append(x)

    for x in y:
        if i != x:
            final.append(x)
        i = x
    
    return final                

unique_in_order('AAAABBBCCDAABBB')
