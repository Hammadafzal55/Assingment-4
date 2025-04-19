def main():

    # Get the temperature in Fahrenheit from the user
    fahrenheit = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0/9.0

    # Print the result
    print(f"Temperature : {fahrenheit}F = {celsius}C")

if __name__ == "__main__":
    main()
# The code above is a simple program that takes a temperature in Fahrenheit as input from the user, converts it to Celsius, and prints the result.