#ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 
# letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

#Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned 
# as they are. Only letters from the latin/english alphabet should be shifted, like in the 
# original Rot13 "implementation".

def rot13(message):
    key, output = "abcdefghijklmnopqrstuvwxyz", ""
    enc = key[13:]+key[:13]
    
    for x in message:
        
        if x.lower() in key:
            if x.islower():
                output += enc[key.find(x)]
            
            else:
                output += str(enc[key.find(x.lower())]).upper()
        
        else:
            output += x
        
    return output

print(rot13("Test"))
