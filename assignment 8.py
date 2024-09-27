class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0



def main():
    # Create a new car with registration number ABC-123 and maximum speed of 142 km/h
    my_car = Car("ABC-123", 142)

    # Print out all the properties of the car
    print(f"Registration Number: {my_car.registration_number}")
    print(f"Maximum Speed: {my_car.max_speed} km/h")
    print(f"Current Speed: {my_car.current_speed} km/h")
    print(f"Travelled Distance: {my_car.travelled_distance} km")


if __name__ == "__main__":
    main()
