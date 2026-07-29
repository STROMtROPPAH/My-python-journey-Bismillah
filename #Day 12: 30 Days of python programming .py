import random
import string

while True:
    try:
        def  random_user_id():

            long = int(input("how long do your user id will be: "))


            return ''.join(random.choices(string.ascii_letters + string.digits, k=long))

        print(random_user_id())


    except ValueError:
        print("please enter a number!!!!!")