def convert_mm_to_cm(value):
    return value / 10.0

def convert_cm_to_mm(value):
    return value * 10.0

def convert_ft_to_m(value):
    return value * 0.3048

def convert_m_to_ft(value):
    return value / 0.3048

def convert_in_to_cm(value):
    return value * 2.54

def convert_cm_to_in(value):
    return value / 2.54

def display_menu():
    print("\nUnit Conversion Menu:")
    print("1. Convert Millimeters to Centimeters")
    print("2. Convert Centimeters to Millimeters")
    print("3. Convert Feet to Meters")
    print("4. Convert Meters to Feet")
    print("5. Convert Inches to Centimeters")
    print("6. Convert Centimeters to Inches")
    print("7. Exit")

def handle_conversion(choice, value):
    if choice == '1':
        return convert_mm_to_cm(value), "cm"
    elif choice == '2':
        return convert_cm_to_mm(value), "mm"
    elif choice == '3':
        return convert_ft_to_m(value), "m"
    elif choice == '4':
        return convert_m_to_ft(value), "ft"
    elif choice == '5':
        return convert_in_to_cm(value), "cm"
    elif choice == '6':
        return convert_cm_to_in(value), "in"
    else:
        return None, None

def main():
    while True:
        display_menu()
        choice = input("Please select an option (1-7): ")

        if choice == '7':
            print("Thank you for using the unit converter. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid option. Please try again.")
            continue

        value = float(input("Enter the value to convert: "))
        converted_value, unit = handle_conversion(choice, value)

        if converted_value is not None:
            print(f"Converted value: {converted_value:.2f} {unit}")
        else:
            print("Error in conversion. Please try again.")

if __name__ == "__main__":
    main()
