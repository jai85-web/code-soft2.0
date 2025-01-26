def calculator():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    print("7. Floor Division (//)")
    print("8. Exit")
    while True:

        choice = input("\nEnter the number of the operation you'd like to perform (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))


                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"The result is: {num1 / num2}")
                elif choice == '5':
                    print(f"The result is: {num1 % num2}")
                elif choice == '6':
                    print(f"The result is: {num1 ** num2}")
                elif choice == '7':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"The result is: {num1 // num2}")
            except ValueError:
                print("Error: Please enter valid numbers.")
        else:
            print("Invalid choice. Please select a valid operation.")

calculator()