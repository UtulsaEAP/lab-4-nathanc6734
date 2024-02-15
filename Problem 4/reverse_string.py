"""
Complete the following python code to reverse the string entered by the user.

Name: Nathan Carr
Lab Time: Thursday @ 2pm
"""

def reverse_string():
    notDone = True
    while notDone:
        entry = input()
        output = ""
        if entry != "done" and entry != "Done" and entry != "d":
            for letter in entry:
                output = letter + output
            print(output)
        else:
            notDone = False
    

if __name__ == "__main__":
    reverse_string()