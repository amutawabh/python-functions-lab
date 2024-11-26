# Exercise 1: Calculate Area of a Triangle
# Function to calculate the area of a triangle
def calculate_area_triangle(base, height):
    return (base * height) / 2

# Test the function
print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
# Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Test the function
print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
# Function to calculate the price after applying a discount
def apply_discount(price, discount):
    return price - (price * discount / 100)

# Test the function
print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature
# Function to convert temperature
def convert_temperature(value, unit):
    if unit == 'C':  # Convert Celsius to Fahrenheit
        return (value * 9/5) + 32
    elif unit == 'F':  # Convert Fahrenheit to Celsius
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

# Test the function
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
# Function to calculate the sum of integers from 1 to n
def sum_to(n):
    return sum(range(1, n + 1))

# Test the function
print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
# Function to find the largest number among three integers
def largest(a, b, c):
    return max(a, b, c)

# Test the function
print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 4, 2))
print('Exercise 6:', largest(-5, 0, -10))

# Exercise 7: Calculate a Tip
# Function to calculate the tip amount
def calculate_tip(bill_amount, tip_percentage):
    return (bill_amount * tip_percentage) / 100

# Test the function
print('Exercise 7:', calculate_tip(50, 20))
print('Exercise 7:', calculate_tip(100, 15))
print('Exercise 7:', calculate_tip(200, 10))

# Exercise 8: Calculate Product of Numbers
# Function to calculate the product of an arbitrary number of numbers
def product(*args):
    result = 1  # Initialize the result to 1 (identity for multiplication)
    for num in args:
        result *= num  # Multiply each number to the result
    return result

# Test the function
print('Exercise 8:', product(2, 5, 5))  # Expected output: 50
print('Exercise 8:', product(-1, 4))    # Expected output: -4
print('Exercise 8:', product(1, 2, 3, 4))  # Expected output: 24
print('Exercise 8:', product())  # Expected output: 1 (no numbers provided)

# Exercise 9: Basic Calculator
# Function to perform basic arithmetic operations
def basicCalculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:  # Prevent division by zero
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Test the function
print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))  # Expected: 5
print('Exercise 9 Result:', basicCalculator(10, 5, "add"))       # Expected: 15
print('Exercise 9 Result:', basicCalculator(10, 5, "multiply"))  # Expected: 50
print('Exercise 9 Result:', basicCalculator(10, 5, "divide"))    # Expected: 2
print('Exercise 9 Result:', basicCalculator(10, 0, "divide"))    # Expected: Error: Division by zero
print('Exercise 9 Result:', basicCalculator(10, 5, "modulo"))    # Expected: Error: Invalid operation


