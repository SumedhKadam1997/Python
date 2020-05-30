def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1*num2 + num2

def difference(num1, num2):
    return num1-num2
while True:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    action = int(input("What would you like to do ?\nAdd, Multiply or Difference\nFor Addition press 1  \nFor Multiply press 2  \nFor Difference press 3  "))

    if action == 1:
        print(add(num1, num2))

    elif action == 2:
        print(multiply(num1, num2))

    elif action == 3:
        print(difference(num1, num2))

    fur_action = input("Would you like to do again ? (y/n) ")
    if fur_action == 'y':
        continue
    else:
        break