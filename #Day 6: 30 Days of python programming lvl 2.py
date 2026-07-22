#reate fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
#Change the about food_stuff_tp tuple to a food_stuff_lt list
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
#Slice out the first three items and the last three items from food_stuff_lt list
#Delete the food_stuff_tp tuple completely turn all this to

fruits = ('ornge', 'durian')
vegetables = ('brocolli', 'cucumber')
animal = ('fish snacks','tuna cibbels')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)


food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle = food_stuff_lt[3]
print(f"middle item is", middle)
print("first three: ", food_stuff_lt[:3])