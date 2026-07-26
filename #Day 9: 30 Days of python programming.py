while True:
    try:
        age = int(input("enter your age: "))
        break
    except ValueError:
        print("please enter number")


if age >= 18:
    print("You are old enough to learn how  to drive: ")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")


while True:
    try:
        age = int(input("enter your age: "))

        if age > 18:
            older_bot = age - 18
            print(f"you are {older_bot} older than me!!")
        elif age < 18:
                younger_bot = 18 - age
                print(f"you are {younger_bot} younger than me!! ")
        else:
            print("we are the same age")
        break
    except ValueError:
        print("enter a number")

