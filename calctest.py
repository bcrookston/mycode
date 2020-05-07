#!/usr/bin/env python3

num1= int(input("First Number?"))
num2= int(input("Second Number?"))
answer = input("What are we doing? \n 1. Adding \n 2.Subtracting \n 3. Multiply \n 4. Divide\n >")

#if isinstance(num1, int) and  isinstance(num2, int)
def mycalc(X,Y,Z):
    if Z=="1":
        sum = num1+num2
        return sum
    elif Z=="2":
        sum = num1 - num2
        return sum
    elif Z=="3":
        sum = num1 * num2
        return sum
    elif Z=="4":
       sum = num1 / num2
       return sum
print(mycalc(num1, num2, answer))

