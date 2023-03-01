"""
28 February 2023
Group B
Charles "Bobby" Barnett
Sonia Flores
Karli Porter
Tyler Sotomayor

                        Midterm Exam 

            Completed in Partial Fulfillment of the Requirements of
            COP 2930 | Select Topics in Computer Programming - Python


Dennis Hunchuck | Valencia College (Spring 2023)

main.py - main program module
autos.py - Autos class module
autos_data.py - data module (for testing)
random_autos.py - random data generator module
"""

from autos import Autos
from autos_data import autos_data
for auto_data in autos_data:
    Autos(**auto_data)

# Define menu selections as constants
MENU_ADD_AUTO = "1"
MENU_DISPLAY_AUTOS = "2"
MENU_STATISTICS = "3"
MENU_EDIT_AUTO = "4"
MENU_QUIT = "Q"

# Define statistics menu selections as constants
STATISTICS_SORT_BY_PRICE = "1"
STATISTICS_SORT_BY_YEAR = "2"
STATISTICS_SORT_BY_FUEL_ECONOMY = "3"
STATISTICS_COUNT_AUTOS = "4"
STATISTICS_AVERAGE_PRICE = "5"
STATISTICS_MOST_EXPENSIVE = "6"
STATISTICS_LEAST_EXPENSIVE = "7"
STATISTICS_RETURN_TO_MAIN_MENU = "M"


def main():
    main_menu()


def main_menu():
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == MENU_ADD_AUTO:
            add_auto()
        elif choice == MENU_DISPLAY_AUTOS:
            sort_by = input("Sort by make (M), model (D), year (Y), fuel economy (F), price (P), or none (N)? ").lower()
            if sort_by == 'n':
                header = "Autos List > Unfiltered > Unsorted"
                print(header)
                display_autos()
            else:
                reverse = input("Sort in ascending (A) or descending (D) order? ").lower() == 'd'
                filter_by = input("Filter by make (press Enter to display all): ")
                display_autos(sort_by, reverse, filter_by)
        elif choice == MENU_STATISTICS:
            statistics_menu()
        elif choice == MENU_EDIT_AUTO:
            edit_auto()
        elif choice == MENU_QUIT:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def add_auto():
    vin = input("Enter vin: ")
    make = input("Enter Make: ")
    model = input("Enter Model: ")
    year = int(input("Enter Year: "))
    fuel_economy = float(input("Enter Fuel Economy (in MPG): "))
    price = float(input("Enter Price: "))
    Autos(vin, make, model, year, fuel_economy, price)
    print("Auto added successfully.")


def average_price():
    autos_list = Autos.get_autos_list()
    if not autos_list:
        print("No autos found.")
    else:
        prices = [auto.get_price() for auto in autos_list]
        avg_price = sum(prices) / len(prices)
        print(f"Average Price of Autos: {avg_price:.2f}")


def count_autos():
    autos_list = Autos.get_autos_list()
    print(f"Number of Autos: {len(autos_list)}")


def display_autos(sort_by=None, reverse=False, filter_by=None):
    autos_list = Autos.get_autos_list()

    if not autos_list:
        print("No autos found.")
    else:
        filtered_list = autos_list

        # Apply filters
        if filter_by:
            filtered_list = list(filter(lambda auto: auto.get_make().lower() == filter_by.lower(), filtered_list))

        # Apply sorting
        if sort_by and sort_by != "n":
            if sort_by == "m":
                filtered_list.sort(key=lambda auto: auto.get_make().lower(), reverse=reverse)
            elif sort_by == "d":
                filtered_list.sort(key=lambda auto: auto.get_model().lower(), reverse=reverse)
            elif sort_by == "y":
                filtered_list.sort(key=lambda auto: auto.get_year(), reverse=reverse)
            elif sort_by == "f":
                filtered_list.sort(key=lambda auto: auto.get_fuel_economy(), reverse=reverse)
            elif sort_by == "p":
                filtered_list.sort(key=lambda auto: auto.get_price(), reverse=reverse)

        # Print header
        if sort_by and sort_by != "n":
            header = "Autos List"
            if filter_by:
                header += f" > Filtered by: Make '{filter_by}'"
            if sort_by:
                sort_key_names = {
                    "m": "Make",
                    "d": "Model",
                    "y": "Year",
                    "f": "Fuel Economy",
                    "p": "Price"
                }
                sort_by_name = sort_key_names[sort_by]
                sort_order_name = "Descending" if reverse else "Ascending"
                header += f" > Sorted by: {sort_by_name} > {sort_order_name}"
            print(header)

        # Print autos
        for auto in filtered_list:
            print(auto)


def edit_auto():
    vin = input("Enter vin of auto to edit: ")
    autos_list = Autos.get_autos_list()
    auto_to_edit = None
    for auto in autos_list:
        if auto.get_vin() == vin:
            auto_to_edit = auto
            break

    if auto_to_edit is None:
        print("Auto not found.")
    else:
        make = input("Enter new Make (press Enter to keep current value): ")
        if make:
            auto_to_edit.set_make(make)

        model = input("Enter new Model (press Enter to keep current value): ")
        if model:
            auto_to_edit.set_model(model)

        year = input("Enter new Year (press Enter to keep current value): ")
        if year:
            auto_to_edit.set_year(year)

        fuel_economy_option = input("Do you want to edit the fuel economy value? (y/n): ")
        if fuel_economy_option.lower() == 'y':
            fuel_economy = input("Enter new Fuel Economy (in MPG): ")
            if fuel_economy:
                auto_to_edit.set_fuel_economy(float(fuel_economy))

        price = input("Enter new Price (press Enter to keep current value): ")
        if price:
            auto_to_edit.set_price(float(price))

        print("Auto edited successfully.")


def least_expensive_auto():
    autos_list = Autos.get_autos_list()
    if not autos_list:
        print("No autos found.")
        return None
    else:
        autos_list.sort(key=lambda auto: auto.get_price())
        return autos_list[0]


def most_expensive_auto():
    autos_list = Autos.get_autos_list()
    if not autos_list:
        print("No autos found.")
        return None
    else:
        autos_list.sort(key=lambda auto: auto.get_price(), reverse=True)
        return autos_list[0]


def print_menu():
    print("\n--- Main Menu ---")
    print(f"{MENU_ADD_AUTO}. Add Auto")
    print(f"{MENU_DISPLAY_AUTOS}. Display All Autos")
    print(f"{MENU_STATISTICS}. Statistics")
    print(f"{MENU_EDIT_AUTO}. Edit Auto")
    print(f"{MENU_QUIT}. Quit")


def print_statistics_menu():
    print("\n--- Statistics Menu ---")
    print(f"{STATISTICS_SORT_BY_PRICE}. Sort Autos by Price")
    print(f"{STATISTICS_SORT_BY_YEAR}. Sort Autos by Year")
    print(f"{STATISTICS_SORT_BY_FUEL_ECONOMY}. Sort Autos by Fuel Economy")
    print(f"{STATISTICS_COUNT_AUTOS}. Number of Autos")
    print(f"{STATISTICS_AVERAGE_PRICE}. Average Price of Autos")
    print(f"{STATISTICS_MOST_EXPENSIVE}. Most Expensive Auto")
    print(f"{STATISTICS_LEAST_EXPENSIVE}. Least Expensive Auto")
    print(f"{STATISTICS_RETURN_TO_MAIN_MENU}. Return to Main Menu")


def sort_autos_by_price(reverse=False):
    autos_list = Autos.get_autos_list()
    if not autos_list:
        print("No autos found.")
    else:
        autos_list.sort(key=lambda auto: auto.get_price(), reverse=reverse)
        print("Autos Sorted by Price:")
        for auto in autos_list:
            print(auto)


def sort_autos_by_year(reverse=False):
    autos_list = Autos.get_autos_list()
    if not autos_list:
        print("No autos found.")
    else:
        autos_list.sort(key=lambda auto: auto.get_year(), reverse=reverse)
        print("Autos sorted by year:")
        for auto in autos_list:
            print(auto)


def sort_autos_by_fuel_economy(reverse=False):
    autos_list = Autos.get_autos_list()
    if not autos_list:
        print("No autos found.")
    else:
        autos_list.sort(key=lambda auto: auto.get_fuel_economy(), reverse=reverse)
        print("Autos Sorted by Fuel Economy:")
        for auto in autos_list:
            print(auto)


def statistics_menu():
    while True:
        print_statistics_menu()
        choice = input("Enter choice: ")
        if choice == STATISTICS_SORT_BY_PRICE:
            reverse = input("Sort in ascending (A) or descending (D) order? ").lower() == 'd'
            sort_autos_by_price(reverse)
        elif choice == STATISTICS_SORT_BY_YEAR:
            reverse = input("Sort in ascending (A) or descending (D) order? ").lower() == 'd'
            sort_autos_by_year(reverse)
        elif choice == STATISTICS_SORT_BY_FUEL_ECONOMY:
            reverse = input("Sort in ascending (A) or descending (D) order? ").lower() == 'd'
            sort_autos_by_fuel_economy(reverse)
        elif choice == STATISTICS_COUNT_AUTOS:
            count_autos()
        elif choice == STATISTICS_AVERAGE_PRICE:
            average_price()
        elif choice == STATISTICS_MOST_EXPENSIVE:
            auto = most_expensive_auto()
            if auto:
                print(f"The most expensive auto is: {auto}")
        elif choice == STATISTICS_LEAST_EXPENSIVE:
            auto = least_expensive_auto()
            if auto:
                print(f"The least expensive auto is: {auto}")
        elif choice == STATISTICS_RETURN_TO_MAIN_MENU:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
