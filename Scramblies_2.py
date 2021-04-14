def scramble(s1, s2):

    for x in s2:
        if s2.count(x) > s1.count(x):
            return False

    return True
        

scramble('wwzpqqsqepi', 'yrisqvwqer')
