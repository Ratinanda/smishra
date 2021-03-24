import os, time                                 #import os and time
def loading():                                  #make a function called loading
    spaces = 0                                      #making a variable to store the amount of spaces between the start and the "."
    while True:                                     #infinite loop
        print("\b "*spaces+".", end="", flush=True) #we are deleting however many spaces and making them " " then printing "."
        spaces = spaces+1                           #adding a space after each print
        time.sleep(0.2)                             #waiting 0.2 secconds before proceeding
        if (spaces>5):                              #if there are more than 5 spaces after adding one so meaning 5 spaces (if that makes sense)
            print("\b \b"*spaces, end="")           #delete the line
            spaces = 0                              #set the spaces back to 0

loading()                  