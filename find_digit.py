#Problem taken from: https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
#14/04/2021

def solve_runes(runes):
    data = runes.split("=")
    
    try:
        eval(data[0].replace("?", str("/3")))
        eval(data[1].replace("?", str("/3")))
        y = 0

    except:
        y = 1

    for x in range (y, 9):
        if eval(data[0].replace("?", str(x))) == int(data[1].replace("?", str(x))):
            return x

    return -1

print(solve_runes("123*45?=5?088"))