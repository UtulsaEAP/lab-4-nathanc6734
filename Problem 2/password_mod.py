"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Nathan Carr
Lab Time: Thursday @ 2pm
"""

def password_mod():
    word = input()
    password = ''
    for x in word:
        if x == "i":
            password += "1"
        elif x == "a":
            password += "@"
        elif x == "m":
            password += "M"
        elif x == "B":
            password += "8"
        elif x == "s":
            password += "$"
        else:
            password += str(x)
    password += "!"
    print(password)

if __name__ == "__main__":
    password_mod()