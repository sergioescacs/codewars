#Implement a function that receives two IPv4 addresses, and returns the number of 
# addresses between them (including the first one, excluding the last one).

#All inputs will be valid IPv4 addresses in the form of strings. The last address 
# will always be greater than the first one.

#NOT FINISHED YET

def ips_between(start, end):
    a, b = 0, 0    
    start = start.split(".")
    end = end.split(".")
    
    #end = list(map(lambda x, y: (int(y)-int(x))*(255**end[::-1].index(y)), start[::-1], end[::-1]))
    for x in start[::-1]:
        a += int(x)*255**start[::-1].index(x)
    
    for y in end[::-1]:
        b += int(y)*255**end[::-1].index(y)
    
    return (b-a)+1

print(ips_between("10.0.0.0", "10.0.0.50"))