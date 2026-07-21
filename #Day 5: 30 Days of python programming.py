word = ['i', 'love', 'coding', 'in', 'python']

first_word = word[0]
middle_word = word[2]
last_word = word[4]
space = ' '

print(len(word))
print(first_word + space + middle_word + space + last_word)

mixed_data_types = ['bob', '67', '176', 'single', 'wall street']
print(mixed_data_types)


companies = ['facebook', 'google', 'microsoft', 'apple', 'ibm', 'Oracle']
#companies.append('nvidia')     adiing list
#companies.insert(2, 'O corp')  adding a list between a list  
companies[4] = companies[4].upper()   #
companies.sort()
companies.sort(reverse=True)
#companies.remove('facebook')

a = companies[0]
b = companies[2]
c = companies[5]
space = ' '


print(companies)
print(len(companies))
#print(a + space + b + space + c)
print(' # '.join(companies))  # google # facebook # apple # Oracle # IBM
print('facebook' in companies) #True

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
