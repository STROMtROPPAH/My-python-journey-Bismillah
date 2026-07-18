Name = "bob"
first_name = "lang"
last_name = "donkey"
Country = "skibidibump"
City = "bobber"
married = False
skills = ["python", "gamer"]
age = 67
favorite_number = 3.14


print("my name is", Name)
print("i am from", Country)
print("in a city called", City)
print(married)
print("my skills are", skills)
print("my age is", age)
print("my favorite number is", favorite_number)

#data type

print("Name type:", type(Name))
print("Country type:", type(Country))
print("City type:", type(City))
print("married type:", type(married))
print("skills type:", type(skills))
print("age type:", type(age))
print("favorite_number type:", type(favorite_number))

#len
if len(first_name) > len(last_name):
    print("first name is longer than last name")
elif len(first_name) < len(last_name):
    print("last name is longer then first name")
else:
    ("lengt name same")


