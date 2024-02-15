"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Nathan Carr
Lab Time: Thursday @ 2pm
"""

def norm():
    numberOfInputs = int(input())
    listString = ""
    newNumberList = []
    for x in range(numberOfInputs):
        listString = listString + input() + " "
    numberList = listString.split()
    maximumValue = float(numberList[0])
    for x in numberList:
        if float(x) > maximumValue:
            maximumValue = float(x)
    for x in numberList:
        newNumberList.append(float(x)/maximumValue)
    for x in newNumberList:
        print(f'{x:.2f}')
        

if __name__ == "__main__":
    norm()