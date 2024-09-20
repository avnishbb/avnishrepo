import random
num_dice = int(input("How many dice would you like to roll? "))
total_sum: int = 0
for _ in range(num_dice):
 dice_roll = random.randint(1, 6)
total_sum += dice_roll
print(f"The total sum of rolling {num_dice} dice is: {total_sum}")
