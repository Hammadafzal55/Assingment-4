def main():

    side1 = float(input("\033[1;3m  Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: \033[0m"))

    perimeter = side1 + side2 + side3

    print(f"The perimeter of the triangle is: {perimeter}") 

if __name__ == "__main__":
    main()
# # The code above is a simple program that takes the lengths of the three sides of a triangle as input from the user, calculates the perimeter, and prints the result.