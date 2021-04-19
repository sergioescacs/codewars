#Challenge taken from: https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python
#15/04/21

def proper_fractions(n):
    data = 0

    for y in range(0, n+1):
        for a in range(2, y+1):
            #print(y, " ", a)
            if n%a == 0 and y%a == 0:
                data += 1
                break
    
    if data == 0:
        return 0
    
    else:
        return n-data

print(proper_fractions(16))