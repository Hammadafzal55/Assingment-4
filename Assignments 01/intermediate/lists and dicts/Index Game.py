def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except:
        return "Invalid slice indices."

def index_game():
    sample_list = ['apple', 42, 'banana', 3.14, 'grape']

    while True:
        print("\nCurrent List:", sample_list)
        print("Choose an operation: access, modify, slice, or quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "access":
            idx = int(input("Enter index to access: "))
            print("Element at index", idx, ":", access_element(sample_list, idx))

        elif choice == "modify":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            result = modify_element(sample_list, idx, new_val)
            if isinstance(result, list):
                print("Modified list:", result)
            else:
                print(result)

        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(sample_list, start, end))

        elif choice == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

# Uncomment to play the game
# index_game()

if __name__ == "__main__":
    index_game()