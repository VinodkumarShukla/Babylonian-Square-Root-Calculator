import math

from tabulate import tabulate


# Function to calculate the square root of a number using the Babylonian method
def babylonian_sqrt(x, epsilon=0.0001):
    if x <= 0:
        raise ValueError("Input value must be greater than zero")

    estimate = x
    while True:
        new_estimate = 0.5 * (estimate + x / estimate)
        if abs(new_estimate - estimate) < epsilon:
            return new_estimate
        estimate = new_estimate

# Function to calculate the square root of a single input value
def calculate_single_square_root():
    while True:
        try:
            x = float(input("Enter a positive integer value: "))
            if x > 0:
                break
            else:
                print("Input must be greater than zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    result = babylonian_sqrt(x)
    formatted_result = "{:.3f}".format(result)

    data = []
    data.append([x, formatted_result])
    headers = ["Value", "Square Root"]
    table = tabulate(data, headers, tablefmt="grid")
    print(table)

# Function to calculate square roots within a specified range
def calculate_range_square_roots():
    while True:
        try:
            min_value = int(input("Enter a positive integer value to start your range: "))
            max_value = int(input("Enter a positive integer value to end your range: "))
            if min_value > 0 and max_value > 0 and min_value <= max_value:
                break
            else:
                print(
                    "Invalid input. Make sure both values are valid positive integers, and the minimum is less than or equal to the maximum.")
        except ValueError:
            print("Invalid input. Make sure both values are valid positive integers.")

    data1 = []
    for x in range(min_value, max_value + 1):
        result = babylonian_sqrt(x)
        formatted_result = "{:.3f}".format(result)
        data1.append([x, formatted_result])

    headers = ["Value", "Square Root"]
    table = tabulate(data1, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    print("Welcome to the Babylonian Square Root Calculator")
    while True:
        # Prompt the user for a choice
        choice = input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively:")

        if choice == "single":
            calculate_single_square_root()
            break
        elif choice == "range":
            calculate_range_square_roots()
            break
