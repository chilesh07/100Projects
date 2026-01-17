import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','&','(',')','*','+']

print('Welcome to Password Generator!!!')
in_letter = int(input('Enter how many letter would you like in your password? \n'))
in_num = int(input('How many numbers numbers would you like ? \n'))
in_sym = int(input('How may symbols would you like ? \n'))

password = ''

for letter in range(1,in_letter+1):
      rand = random.choice(letters)
      password += rand

for num in range(1,in_num+1):
      rand = random.choice(numbers)
      password += rand

for sym in range(1,in_sym+1):
      rand = random.choice(symbol)
      password += rand
# print(password)

## method 2

passwords_list = []

for letter in range(1,in_letter+1):
      rand = random.choice(letters)
      passwords_list.append(rand)

for num in range(1,in_num+1):
      rand = random.choice(numbers)
      passwords_list.append(rand)

for sym in range(1,in_sym+1):
      rand = random.choice(symbol)
      passwords_list.append(rand)
      print(passwords_list)

random.shuffle(passwords_list)
print(passwords_list)

rand_pass= ''
for char in passwords_list:
    rand_pass +=char

print(f"Your password is :{rand_pass}")