#Write a function that when given an URL as a string, parses out just the domain name and 
# returns it as a string.

def domain_name(url):
    final = ""

    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")

    for x in url:
        if x != ".":
            final += x

        if x == ".":
            break
    
    return final

domain_name("https://www.cnet.com")
