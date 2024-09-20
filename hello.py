import random
num_dice = int(input("How many dice would you like to roll? "))
total_sum: int = 0
for _ in range(num_dice):
 dice_roll = random.randint(1, 6)
total_sum += dice_roll
print(f"The total sum of rolling {num_dice} dice is: {total_sum}")
numbers = []
while True:
 user_input = input("Enter a number (or press Enter to quit): ")
 if user_input == "":
  break
 try:
  number = int(user_input)
  numbers.append(number)
 except ValueError:
  print("Please enter a valid number.")
numbers.sort(reverse=True)
top_five = numbers[:5]
print("The five greatest numbers are:", top_five)


# Function to check if a number is prime
def is_prime(number):
 # A prime number must be greater than 1
 if number <= 1:
  return False

 # Check if the number has divisors other than 1 and itself
 for i in range(2, int(number ** 0.5) + 1):  # Only check up to the square root of the number
  if number % i == 0:
   return False

 return True


# Ask the user for an integer input
try:
 num = int(input("Enter an integer: "))

 # Check if the number is prime
 if is_prime(num):
  print(f"{num} is a prime number.")
 else:
  print(f"{num} is not a prime number.")
except ValueError:
 print("Please enter a valid integer.")
