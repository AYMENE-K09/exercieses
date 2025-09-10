my_fav_numbers = {18, 20, 30}
my_fav_numbers.add(1)
my_fav_numbers.add(2)
my_fav_numbers.remove(2)

friend_fav_numbers = {28, 33}
friend_fav_numbers.add(5)
friend_fav_numbers.add(8)

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)
