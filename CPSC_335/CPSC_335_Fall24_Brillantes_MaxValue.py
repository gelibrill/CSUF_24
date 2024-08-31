# Function to find the maximum value in a list
def find_max(L):
    maxValue = L[0]
    for n in L[1:]:
        if n > maxValue:
            maxValue = n
    return maxValue

# Function to find the minimum value in a list
def find_min(L):
    minValue = L[0]
    for n in L[1:]:
        if n < minValue:
            minValue = n
    return minValue

# Fucntion to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_input = input("Enter numbers separated by spaces: ")
L = list(map(int, user_input.split()))

choice_input = input(f"Would you like the minimum or maximum value?: (min or max) ").strip().lower()
if choice_input == "min":
    selected_number = find_min(L)
    print("Minimum: ", selected_number, "\n")
elif choice_input == "max":
    selected_number = find_max(L)
    print("Maximum: ", selected_number, "\n")
else:
    print("Invalid choice. Please specify 'min' or 'max'.")

if selected_number is not None:
    factorial_choice = input(f"Would you like the factorial? (y or n) ").strip().lower()
    if factorial_choice == "y":
        print("Factorial of {selected_number} is: ", factorial(selected_number), "\n")
    elif factorial_choice == "n":
        print("Okay :( Maybe next time...\nfactorial has been skipped.\n")
    else:
        print("Invalid input. I don't know what you're asking from me. :/ \n")