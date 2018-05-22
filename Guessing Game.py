# A Guess the word game

import random # this is to let us pick a random word


print("Rules")
print("Guess the word that is provided")
print("you can guess the word 6 times wrong")
print("Make sure that you guess anwser in Caps")
print("")
print("1 - random words")
print("2 - states of america")
print("")
Game = input("What is your choice? =>")
print("")

#1 = words
#2 = States_of_USA

#1 = words
if Game == 1:

    words = ["WORD", "SCHOOL", "SKITTLES", "WATER","LEDGEND"]
    random.shuffle(words) # this code shuffels the words around so you dont get the same one again

    
    Guesses = ""

    Turns = 6

    while Turns > 0:
        Guesses_Wrong = 0

        for char in words[0]: # the [0] picks a number from words and then displays it as the word that the person has to guess
            if char in Guesses:
                print char,
            
            else:
                print"_",

                Guesses_Wrong = Guesses_Wrong + 1
    
        print("")# this is here so that the , in print"_" dosent go in the same line as Guess
    
        if Guesses_Wrong == 0:
            print ("you won")
            #skips the code
            break
    
    
        Guess = raw_input("What is your Guess? =>")
        print("")
        Guesses += " " + Guess

        # this is for if you get the word wrong
        if Guess not in words[0]:
            Turns -= 1
            print("You Guessed Wrong")

            print("you have"),
            print Turns ,
            print("Guesses Left")
    
            if Turns == 0:
                print("")
                print("Game over")
                print("The word Was"),
                print words[0]
                print("")


     
        # this shows you what you already have guessed
        print("word Guessed ="),
        print Guesses
        print("")




#2 = States_of_USA
if Game == 2:
    
    States_of_USA = ["ALABAMA","ALASKA","ARIZONA","ARKANSAS","CALIFORNIA","CLOLRADO","CONNECTICUT","DELAWARE","FLORIDA","GEORGIA","HAWAII","IDAHO","ILLINOIS","INDIANA","IOWA","KANSAS","KENTUCKY","LOUISIANA","MAINE","MARYLAND","MASSACHUSETTS","MICHIGAN","MISSISSIPPI","MISSOURI","MONTANA","NEBRASKA","NEVADA","NEW HAMPSHIRE","NEW JERSEY","NEW MEXICO","NEW YORK","NORTH CAROLINA","NORTH DAKORA","OHIO","OKLAHOMA","OREGON","PENNSYLVANIA","RHODE ISLAND","SOUTH CAROLINA","SOUTH DAKOTA","TENNESSE","TEXAS","UTAH","VERMONT","VIRGINIA","WASHINGTON","WEST VIRGINIA","WISCONSIN","WYOMING"]
    random.shuffle(States_of_USA) # this code shuffels the words around so you dont get the same one again
    
    Guesses = ""

    Turns = 6

    while Turns > 0:
        Guesses_Wrong = 0

        for char in States_of_USA[0]: # the [0] picks a number from words and then displays it as the word that the person has to guess
            if char in Guesses:
                print char,
            
            else:
                print"_",

                Guesses_Wrong = Guesses_Wrong + 1
    
        print("")# this is here so that the , in print"_" dosent go in the same line as Guess
    
        if Guesses_Wrong == 0:
            print ("you won")
            break # THIS SKIPS THE CODE
    
    
        Guess = raw_input("What is your Guess? =>")
        print("")
        Guesses += " " + Guess

        # this is for if you get the word wrong
        if Guess not in States_of_USA[0]:
            Turns -= 1
            print("You Guessed Wrong")

            print("you have"),
            print Turns ,
            print("Guesses Left")
    
            if Turns == 0:
                print("")
                print("Game over")
                print("The word Was"),
                print States_of_USA[0]
                print("")

     
        # this shows you what you already have guessed
        print("word Guessed ="),
        print Guesses
        print("")
            
