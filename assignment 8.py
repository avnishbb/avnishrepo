import random


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


# Main program for car race
def main():
    # Initialize a list of 10 car objects with random max speeds
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    race_finished = False
    hour_count = 0

    # Simulate the race
    while not race_finished:
        hour_count += 1
        print(f"--- Hour {hour_count} ---")

        # Adjust speed and drive for each car
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

            # Check if any car has reached or exceeded 10,000 km
            if car.travelled_distance >= 10000:
                race_finished = True

    # Print results
    print("\nRace finished!")
    print(f"The race took {hour_count} hours.\n")

    # Display the car properties in a formatted table
    print(f"{'Registration':<12}{'Max Speed (km/h)':<18}{'Current Speed (km/h)':<20}{'Travelled Distance (km)'}")
    print("-" * 64)
    for car in cars:
        print(f"{car.registration_number:<12}{car.max_speed:<18}{car.current_speed:<20}{car.travelled_distance:.1f}")


if __name__ == "__main__":
    main()
