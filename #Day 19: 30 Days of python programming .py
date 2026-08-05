def is_valid_variable(var):
    return var.isidentifier()

print(is_valid_variable('first_name'))   
print(is_valid_variable('first-name'))   
print(is_valid_variable('1first_name'))  
print(is_valid_variable('firstname'))    