#*====================================================================================================================
#|   Assignment:  Problem Set 6 - Mario/less
#|       Author:  Slavko Mihajlovic
#|     Language:  C
#|   To Compile:  Run the make file
#|
#|        Class:  CS50: Introduction to Computer Science -Harvard University 
#|   Instructor:  David J. Malan
#|     Due Date:  April 2020
#|
#|+--------------------------------------------------------------------------------------------------------------------
#|
#|  Description:  Prints out a piramid on the terminal
#|        Input:  run python mario.py
#|               
#|       Output:  # piramid
#|
#|    Algorithm:  N/A
#|      
#|
#|   Required Features Not Included:  No requirmant.
#|      
#|
#|   Known Bugs:  N/A
#|      
#|
#|*====================================================================================================================*/

from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        width = height + 1
        if height > 0 and height <= 8:
            break

    for i in range(1, height):
        num_hashes = i 
        num_spaces = width - num_hashes

        print(" " * num_spaces, end="")
        print("#" * num_hashes)


if __name__ == "__main__":
    main()
