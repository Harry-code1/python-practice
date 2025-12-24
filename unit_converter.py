def show_menu():
    print("Unit Converter")
    print("1 - Kilometres to Miles")
    print("2 - Miles to Kilometres")
    print("3 - Kilograms to Pounds")
    print("4 - Pounds to Kilograms")

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def main():
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        km = get_number("Enter kilometres: ")
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif choice == "2":
        miles = get_number("Enter miles: ")
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")
    elif choice == "3":
        kg = get_number("Enter kilograms: ")
        print(f"{kg} kg = {kg_to_pounds(kg):.2f} pounds")
    elif choice == "4":
        pounds = get_number("Enter pounds: ")
        print(f"{pounds} pounds = {pounds_to_kg(pounds):.2f} kg")
    else:
        print("Invalid option.")

main()
