class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    # Method to change the car's speed
    def accelerate(self, speed_change):
        # Adjust speed, ensuring it stays within 0 and max_speed
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    # Method to drive the car for a given number of hours
    def drive(self, hours):
        # Update travelled distance based on current speed and time
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed of 142 km/h
    my_car = Car("ABC-123", 142)

    # Simulate a pre-existing travelled distance (2000 km)
    my_car.travelled_distance = 2000
    print(f"Initial Travelled Distance: {my_car.travelled_distance} km")

    # Accelerate the car
    my_car.accelerate(60)  # Set speed to 60 km/h
    print(f"Current Speed: {my_car.current_speed} km/h")

    # Drive the car for 1.5 hours
    my_car.drive(1.5)
    print(f"Travelled Distance after 1.5 hours: {my_car.travelled_distance} km")


if __name__ == "__main__":
    main()
