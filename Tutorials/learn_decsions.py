import random 

number = random.randint(0, 10)

print(number)

if (number < 7):
    print("number is lesser than 7")

elif(number > 7):
    print("number is greater than 7")
    
else:
    print("number is 7")
    
################################

numbers = [random.randint(0, 10) for i in range(0, 10)]

print(numbers)

if(7 in numbers):
    print("7 is in")
    
else:
    print("7 is not in")
    
    