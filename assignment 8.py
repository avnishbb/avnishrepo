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


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed of 142 km/h
    my_car = Car("ABC-123", 142)

    # Accelerate the car in steps
    my_car.accelerate(30)
    print(f"Current Speed after +30 km/h: {my_car.current_speed} km/h")

    my_car.accelerate(70)
    print(f"Current Speed after +70 km/h: {my_car.current_speed} km/h")

    my_car.accelerate(50)
    print(f"Current Speed after +50 km/h: {my_car.current_speed} km/h")

    # Apply emergency brake (-200 km/h)
    my_car.accelerate(-200)
    print(f"Current Speed after emergency brake: {my_car.current_speed} km/h")
