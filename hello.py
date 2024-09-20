
seasons = ("winter", "winter", "spring", "spring", "spring",
           "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")
try:
    month = int(input("Enter the number of a month (1-12): "))
    if 1 <= month <= 12:
        print(f"The season is: {seasons[month - 1]}")
    else:
        print("Please enter a valid month number between 1 and 12.")
except ValueError:
    print("Please enter a valid integer.")

