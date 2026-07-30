numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_nums = [i for i in numbers if i <= 0 ]
print(negative_nums)




list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 # T
 # 1
 # v
seperate = [num for row in list_of_lists for num in row]
print(seperate)




names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
mix = [names[0] for row in names for names in row]
print(mix)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
mix = [countries for row in countries for countries in row]
print(mix)  