#!/usr/bin/python3
mynum = 0
mynum2 = 0
answer = " "
answer2 = " "
while mynum < 2:
    mynum += 1     # increase the round counter by 1
    answer = input("Please choose the correct Rush Album \n 1. 1984\n 2.Out OF Exile\n 3. Above\n 4. 2112\n Your Guess:  ")
    if answer == "4":
        print("Good Job lets do another")
        break
    elif answer != "4":
        print("Sorry, the answer was 4.")
