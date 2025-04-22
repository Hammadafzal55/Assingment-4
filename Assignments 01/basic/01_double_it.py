def main():
    number = int(input("Eneter a number"))
    current_number = 1
    while current_number < 100:
        current_number = current_number * number
        print(current_number)


if __name__ == '__main__':
    main()