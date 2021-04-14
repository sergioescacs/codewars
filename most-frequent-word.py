#Write a function that, given a string of text (possibly with punctuation and line-breaks), 
# returns an array of the top-3 most occurring words, in descending order of the number of 
# occurrences.

#Assumptions:

#A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. 
# (No need to handle fancy punctuation.)
#Matches should be case-insensitive, and the words in the result should be lowercased.
#Ties may be broken arbitrarily.
#If a text contains fewer than three unique words, then either the top-2 or top-1 words should 
# be returned, or an empty array if a text contains no words.


def top_3_words(text):
    
    y = 0
    top3 = {}
    lista1 = ""
    dic = "abcdefghijklmnopqrstuvwxyz" #dictionary to compare string characters with abecedary 
    
    text = text.lower() #converting all string characters to the same type  
    
    #first loop to remove non possible key-letters on english possible words using the dictionary    
    for x in text:
        if x in dic or x == " ":
            lista1 += x
            
        elif x == "'":
            if text[y+1] in dic or text[y-1] in dic:
                lista1 += x
        
        else:
            lista1 += " "
        y += 1
    
    #converting the string to array
    lista1 = lista1.split(" ")
    
    #removing blank gaps 
    lista1 = [x for x in lista1 if x]
    
    #second loop, counting all words and adding them into a dictionary [data]
    for z in lista1:
        y = lista1.count(z)
        
        if z not in top3:
            top3["%s" % z]= y

    #sorting and choosing the necesari data 
    top3 = list(map(lambda x: x[0], sorted(top3.items() , reverse= True,  key=lambda x: x[1])))
    
    #removing the unecesary data
    while len(top3) > 3:
        top3.pop()

    #returning the final results 
    return top3