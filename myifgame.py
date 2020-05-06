#!/usr/bin/python3
mynum = 0
mynum2 = 0
move_on = "NO"

while mynum < 2 or answer !="4" :
    mynum += 1     # increase the round counter by 1
    answer = input("Please choose the correct Rush Album \n 1. 1984\n 2.Out OF Exile\n 3. Above\n 4. 2112\n Your Guess:  ")
    if answer == "4":
        print("Good Job lets do another")
        while mynum2 < 2 or answer2 != "3":
            mynum2 +=1
            answer2 = input("\nPlease choose another Rush album\n 1.See The Light\n 2.Throwing Copper\n 3 Power Windows\n 4.Dark Side Of The Moon ")
            if answer2 == "3":
                print("Great Job")           
            elif answer2 != "3":
                print("Sorry, the answer was 4")
    elif answer != "4":
     print("Sorry, the answer was 4.")
     
#if move_on =="YES":
 #   while mynum2 < 2:
  #       mynum2 += 1     # increase the round counter by 1
   #      answer2 = input("\nPlease choose another Rush album\n 1.See The Light\n 2.Throwing Copper\n 3 Power Windows\n 4.Dark Side Of The Moon ")
          #if answer2 == "3":
         # print("Good Job lets do another")
         # break
         # elif answer2 != "4":
         # print("Sorry, the answer was 4.")
