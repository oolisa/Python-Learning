#!/usr/bin/env python3.7
#Scenario : 
# typical Fizz-Buzz problem goes like this:
#Write a program that prints the numbers from 1 - 100. For each multiple of three print "Fizz" instead of the number. For multiples of five print "Buzz" instead of the number. If a number is a multiple of three and five then print "FizzBuzz". Solving this problem requires 2 key components: looping and conditionals.
#We're going to write a script that prompts the user for the number of items to process (starting with 1). For each number, we'll print either "Fizz", "Buzz", "FizzBuzz", or the number. The criteria for what to print is:
#Print "FizzBuzz" if the number is divisible by 3 and 5.
#Print "Fizz" if the number is divisible by 3.
#Print "Buzz" if the number is divisible by 5.
#Otherwise print the number.

upper_number = int(input("How many values should we process:"))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    