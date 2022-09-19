# Computer Quiz made by Fred
# This quiz was coded by myself alough I did use google to get around some of the errors I was having

from operator import contains
import time # allows us to wait before starting a new question

playingtrue = input("Would you like to start?   ") # Asking the user to input - while printing "Would you like to start?"

if playingtrue == "no":  # if the answers are equal to yes, sure or start it will continue down the code.
    quit()  # If any other answer is given it will quit the program;

print("Okay lets go!") # If Yes, sure or start is given it shall print.



time.sleep(1) # waiting 1 second

question1 = input("What does CPU Stand for?  ") # Asking for a input - while printing 
if question1 == "central processing unit":    #Defining the correct answer
    print("Correct!")  # If correct answer is given this shall be printed
    count =+1 # adding +1 to the count to allow us to gather this score later.

else:
    print("Incorrect")  # if the answer is incorrect this will print

time.sleep(1) # waiting 1 second

question2 = input("What does RAM Stand for?  ") # Asking for a input - while printing 
if question2 == "random access memory": #Defining the correct answers
    print("Correct!")  # If correct answer is given this shall be printed
    count =+1 # adding +1 to the count to allow us to gather this score later.

else:
    print("Incorrect")  # if the answer is incorrect this will print

time.sleep(2) # waiting 1 second
print("Quiz over!") 


if count == 1: 
    print("Unlucky, Try again. you got 1 ") # will send this is the score is 1

if count == 2:
    print("Amazing job! you got", count) # will send this if the score is 2

else: 
    print("Unlucky, you got 0") #if the score is 0 it will send this


   






