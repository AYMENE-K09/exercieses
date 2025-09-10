the_enough_height = int(145)
user_height = int(input("enter your height by cm: "))

if user_height > the_enough_height:
    print(f"your height is {user_height}, it is enough to ride.")

else:
    print(f"your height is {user_height}, you need to grow some more to ride.")
