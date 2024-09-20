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

