import hashlib
import pyperclip
 
def hash(str):
    return hashlib.sha256(str).hexdigest()
    

while True:
    site = input("Site: ")
    username = input("Username: ")
    password = input("Password: ")

    normal = hash(site + username + password)
    special = hash(username + password + site)
    upper = hash(password + site + username)
    num = hash(password + username + site)

    result = ""


    for i in range(6):
        if ord(normal[i]) > 96:
            result += normal[i]
        else:
            result += chr(ord(normal[i]) + 49)

        if ord(special[i]) > 96:
            result += chr(ord(special[i]) - 64)
        else:
            result += chr(ord(special[i]) - 15)

        if ord(upper[i]) > 96:
            result += chr(ord(upper[i]) - 32)
        else:
            result += chr(ord(upper[i]) + 17)

        if ord(num[i]) > 96:
            result += chr(ord(num[i]) - 49)
        else:
            result += num[i]
            
    print("\n" + result[:18] + " " + result[18:])
    pyperclip.copy(result[:18])
    print("First 20 characters have been copied to clipboard\n")
    
