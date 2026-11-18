print("=== Smart Home Controller ===")
while True:
    print("\n1. Motion Detection")
    print("2. Temperature Check")
    print("3. Door Status")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        motion = input("Is motion detected? (yes/no): ").lower()
        if motion == "yes":
            print("Motion detected!")
            print("Light turned ON.")
        else:
            print("No motion detected.")
            print("Light turned OFF.")
    elif choice == "2":
        temp = int(input("Enter room temperature (°C): "))
        if temp >= 30:
            print("Temperature is high.")
            print("Fan turned ON.")
        else:
            print("Temperature is normal.")
            print("Fan turned OFF.")
    elif choice == "3":
        door = input("Is the door open? (yes/no): ").lower()
        if door == "yes":
            print("Door is open.")
            print("Security Alarm ON.")
        else:
            print("Door is closed.")
            print("Security Alarm OFF.")
    elif choice == "4":
        print("Exiting Smart Home Controller...")
        break
    else:
        print("Invalid choice! Try again.")
