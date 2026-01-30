a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = input("Choose operation: ")

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
elif choice == "3":
    print(a * b)
elif choice == "4":
    print(a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid choice")