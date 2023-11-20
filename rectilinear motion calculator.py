import math

def calculate_displacement(initial_position, final_position):
    return final_position - initial_position

def calculate_velocity(initial_position, final_position, time):
    return (final_position - initial_position) / time

def calculate_acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

def main():
    while True:
        print("Select operation:")
        print("1. Calculate Displacement")
        print("2. Calculate Velocity")
        print("3. Calculate Acceleration")
        print("4. Quit")

        choice = input("Enter choice(1/2/3/4): ")

        if choice == '1':
            initial_position = float(input("Enter initial position: "))
            final_position = float(input("Enter final position: "))
            print("Displacement: ", calculate_displacement(initial_position, final_position))

        elif choice == '2':
            initial_position = float(input("Enter initial position: "))
            final_position = float(input("Enter final position: "))
            time = float(input("Enter time: "))
            print("Velocity: ", calculate_velocity(initial_position, final_position, time))

        elif choice == '3':
            initial_velocity = float(input("Enter initial velocity: "))
            final_velocity = float(input("Enter final velocity: "))
            time = float(input("Enter time: "))
            print("Acceleration: ", calculate_acceleration(initial_velocity, final_velocity, time))

        elif choice == '4':
            print("Exiting the calculator")
            break

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()