def remove_duplicates_preserve_order(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


def remove_duplicates_set(lst):
    return list(set(lst))


while True:
    print("\n--- Duplicate Remover ---")
    print("1. Remove duplicates (Preserve Order)")
    print("2. Remove duplicates (Fast Method)")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1' or choice == '2':
        user_input = input("Enter elements separated by space: ")
        data = user_input.split()

        if choice == '1':
            result = remove_duplicates_preserve_order(data)
        else:
            result = remove_duplicates_set(data)

        print("Result:", result)

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
