"""
Code a Python program that will read from the text file inventory.txt and
perform the following on the data, to prepare for presentation to your
managers: My last capston project Banze billy.
    
"""
from tabulate import tabulate  # Make sure to install this module using: pip install tabulate

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} | {self.code} | {self.product} | Cost: {self.cost} | Quantity: {self.quantity}"

shoes_list = []

def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the header
            for line in file:
                data = line.strip().split(',')
                shoes_list.append(Shoe(data[0], data[1], data[2], int(data[3]), int(data[4])))
    except FileNotFoundError:
        print("File not found.")

def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = int(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoes_list.append(Shoe(country, code, product, cost, quantity))

def view_all():
    print(tabulate([shoe.__dict__ for shoe in shoes_list], headers="keys", tablefmt="grid"))

def re_stock():
    lowest_quantity_shoe = min(shoes_list, key=lambda x: x.quantity)
    print(f"The shoe with the lowest quantity is: {lowest_quantity_shoe}")
    add_quantity = int(input("Enter the quantity to add: "))
    lowest_quantity_shoe.quantity += add_quantity
    print("Quantity updated.")

def search_shoe(code):
    for shoe in shoes_list:
        if shoe.code == code:
            return shoe
    return None

def value_per_item():
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: {value}")

def highest_qty():
    highest_quantity_shoe = max(shoes_list, key=lambda x: x.quantity)
    print(f"The shoe with the highest quantity is: {highest_quantity_shoe.product} | Quantity: {highest_quantity_shoe.quantity} | For Sale!")

def main():
    read_shoes_data()

    while True:
        print("\n===== Menu =====")
        print("1. View All Shoes")
        print("2. Add Shoe")
        print("3. Re-stock Shoes")
        print("4. Search Shoe by Code")
        print("5. Calculate Value per Item")
        print("6. Find Shoe with Highest Quantity")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            code = input("Enter shoe code to search: ")
            result = search_shoe(code)
            if result:
                print(result)
            else:
                print("Shoe not found.")
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
