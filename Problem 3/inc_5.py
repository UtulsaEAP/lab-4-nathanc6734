"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Nathan Carr
Lab Time: Thursday @ 2pm
"""

def inc_5():
    first_number = int(input())
    second_number = int(input())
    output = ""
    if first_number < second_number:
        x = range(first_number, second_number, 5)
        for i in x:
            output = output + str(i) + " "
        if (second_number - first_number) % 5 == 0:
            output = output + str(second_number)
        print(output + "\n")
    elif first_number == second_number:
        print(str(first_number) + "\n")
    else:
        print("Second integer can't be less than the first.")

        
    



if __name__ == '__main__':
    inc_5()