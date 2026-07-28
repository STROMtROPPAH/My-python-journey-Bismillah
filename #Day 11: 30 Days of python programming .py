def circle_area():
    enter_number = int(input("please enter radius: "))
    pie = 3.14
    penyelesaian = enter_number * enter_number * pie 
    return penyelesaian
print("the answer to your number is: ", circle_area())


#list
def remove_item():
    food_stuff = []
    while True:
        enter = input("please enter food to list: ")
        food_stuff.append(enter)
        question = input("do you want to add more? or do you wanna see the list? type list: ")
        if question == "yes":
            enter = input("please enter food to list: ")
            food_stuff.append(enter)
            print(food_stuff)
        elif question == "list":
            print(food_stuff)
        elif question == "no":
            break
    return food_stuff
print("item has been added to list", remove_item()) 