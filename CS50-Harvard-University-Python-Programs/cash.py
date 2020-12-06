# *====================================================================================================================
# |   Assignment:  Problem Set 6 - Cash Python
# |       Author:  Slavko Mihajlovic
# |     Language:  C
# |   To Compile:  Run the make file
# |
# |        Class:  CS50: Introduction to Computer Science -Harvard University 
# |   Instructor:  David J. Malan
# |     Due Date:  April 2020
# |
# |+--------------------------------------------------------------------------------------------------------------------
# |
# |  Description:  N/A
# |        Input:  N/A
# |               
# |       Output:  N/A
# |    Algorithm:  N/A
# |      
# |
# |   Required Features Not Included:  No requirmant.
# |      
# |
# |   Known Bugs:  N/A
# |      
# |
# |*====================================================================================================================*/
from cs50 import get_float
from math import floor


def main():
    while True:
        dollars_owed = get_float("Change owed: ")
        cents_owed = floor(dollars_owed * 100)

        if cents_owed > 0:
            break

    quarters = cents_owed // 25
    dimes = (cents_owed % 25) // 10
    nickels = ((cents_owed % 25) % 10) // 5
    pennies = ((cents_owed % 25) % 10) % 5

    print(f"{quarters + dimes + nickels + pennies}")


if __name__ == "__main__":
    main()
