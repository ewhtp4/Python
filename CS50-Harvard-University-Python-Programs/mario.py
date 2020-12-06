# *====================================================================================================================
# |   Assignment:  Problem Set 5 - Speller -Hash
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
# |  Description:  Implements a dictionary's functionality
# |        Input:  (example)./speller texts/lalaland.txt
# |               
# |       Output:  A terminal output stateing the number of misspelled words in the gven text
# |
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



from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        width = height
        if height >= 0 and height <= 23:
            break

    for i in range(1, height + 1):
        num_hashes = i
        num_spaces = width - num_hashes

        print(" " * num_spaces, end="")
        print("#" * num_hashes, end="")

        print("  ", end="")

        print("#" * num_hashes)


if __name__ == "__main__":
    main()
