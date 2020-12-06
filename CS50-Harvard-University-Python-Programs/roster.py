# *====================================================================================================================
# |   Assignment:  Problem Set 7 - Roster Python
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

from cs50 import SQL
from sys import argv

# check that we launched the code with proper arguments, otherwise it exits the program
if len(argv) < 2:
    print("usage error, roster.py houseName")
    exit()

# open the database in a variable and then execute a query that list all the people from a particular house in alphabetical order
db = SQL("sqlite:///students.db")
students = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last", argv[1])

# print each person showing their information and their middle name if they have one
for student in students:
    if student['middle'] != None:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['last']}, born {student['birth']}")
