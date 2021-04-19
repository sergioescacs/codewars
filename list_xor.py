# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.

# Your function must return whether n is exclusively in list1 or list2.
# In other words, if n is in both lists or in none of the lists, return False. If n is in only one 
# of the lists, return True.

#Challenge taken from: https://pythonprinciples.com/challenges/List-xor/ 19/04/21

def list_xor(n, list1, list2):
    
    if n in list1 and n not in list2 or n not in list1 and n in list2:
        return True

    else:
        return False

print(list_xor(1, [1, 2, 3], [1, 5, 6])) 