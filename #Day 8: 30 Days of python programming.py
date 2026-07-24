cat_dct = {
    'name' : 'kenzo',
    'color' : 'orange',
    'breed' : 'persian mix maicooon',
    'age' : '4years',

}

student_dct = {
    'first_name' : 'bober',
    'last_name' : 'sober',
    'gender' : 'males',
    'age' : '67',
    'country' : 'skibidibump',
    'city' : 'Ohio',

}
#adding stuff
student_dct['hobby'] = 'playing drone'
student_dct['skill'] = 'playing lego'
#Getting Dictionary Keys as a List
values = student_dct.keys()
#Getting Dictionary Values as a List
values = student_dct.values()

print(len(student_dct))
print('first_name' in student_dct)
print(student_dct.items())
print("the keys are:", list(student_dct.keys()))
print("the value are:", list(student_dct.values()))

print(student_dct.items())