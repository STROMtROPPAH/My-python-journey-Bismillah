
#Declare your age as integer variable
try: 
    Age = int(input("enter your age: "))
    height = int(input("enter your height in cm: "))
    weight = int(input("enter your weight in kg: "))

    height_m = height / 100
    bmi = weight / (height_m**2)

    print("your bmi is", bmi)


except ValueError:
    print("please enter a number!!")
    (exit)

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
     print("Obese")

#perimeter of a triangle 
try:
    Enter_side_a = int(input("enter side a: "))
    Enter_side_b = int(input("enter side b: "))
    Enter_side_c = int(input("enter side c: "))
    print("the area of your triangle perimeter is:", Enter_side_a + Enter_side_b + Enter_side_c)

except ValueError:
    print("please enter a number!!")
    sys.exit()

#base and height
try:
    a = int(input("enter the base of your triangle: "))
    b = int(input("enter the height of your triangle: "))
    
    print("total area of your triangle based on your input is:", (a * b) / 2 )

except ValueError:
    print("please enter a number!!")
    sys.exit()

#Write a script that prompts the user to enter number of years.
try:
    a = int(input("Enter number of years you have lived: "))
    print(f"{a * 365 * 86400 }seconds thats how long you live in this world congrats")

except ValueError:
    print("please enter a number!!")
    (exit)