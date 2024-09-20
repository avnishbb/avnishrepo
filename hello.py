airports = {}

def add_airport():
    """Function to add a new airport."""
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    name = input("Enter the name of the airport: ")
    airports[icao_code] = name
    print(f"Airport {name} with ICAO code {icao_code} added successfully!")
def fetch_airport():
    """Function to fetch information of an existing airport."""
    icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()
    if icao_code in airports:
        print(f"The airport with ICAO code {icao_code} is {airports[icao_code]}.")
    else:
        print(f"No airport found with ICAO code {icao_code}.")
def main():
    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch information of an existing airport")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, 3): ")
        if choice == '1':
            add_airport()
        elif choice == '2':
            fetch_airport()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")
main()



