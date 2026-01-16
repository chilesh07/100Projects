import random
import my_model


random_integer = random.randint(1, 2)
print(random_integer)
random_number0_1 = random.random() ##  it provides has only number between the 0 to 1 with the floating values
print(random_number0_1)
print(my_model.favourite_number)

if random_integer == 1 :
    print("Heads")
else:
    print("Tails")

state_fruits = my_model.favourite_fruits
print(state_fruits[::-1])

# challenges
friends = ['Alice', 'Bob', 'Charlie','David','Emanuel']
print(len(friends))
pick_one  = random.choice(friends)
print(pick_one)

favorite_list = [my_model.favourite_vegetables,my_model.favourite_fruits]
print(favorite_list)
