class InventoryItem:
    def _init_(self, name, price):
        self.name = name
        self.price = price

inventory = {
    "pen": InventoryItem("pen", 10),
    "pencil": InventoryItem("pencil", 5),
    "rubber": InventoryItem("rubber", 5),
    "notebook": InventoryItem("notebook", 50),
    "book": InventoryItem("book", 100)
}

cart = {}

def display_inventory():
    print("Inventory Items:")
    for item in inventory.values():
        print(f"{item.name.capitalize()} - Rs. {item.price}")

def add_to_cart(item, quantity):
    if item in inventory:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {item}(s) added to cart.")
    else:
        print("Item doesn't exist. Please enter a valid item name.")

def display_cart():
    print("\nCart:")
    total_amount = 0
    for item, quantity in cart.items():
        item_price = inventory[item].price
        total_item_amount = item_price * quantity
        total_amount += total_item_amount
        print(f"{quantity} {item}(s) - Rs. {total_item_amount}")
    print(f"Total Amount: Rs. {total_amount}")
    return total_amount

def main():
    display_inventory()
    while True:
        item = input("\nEnter the item you want to buy: ").lower()
        if item not in inventory:
            print("Item doesn't exist. Please enter a valid item name.")
            continue
        try:
            quantity = int(input("Enter the quantity: "))
            add_to_cart(item, quantity)
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
            continue
        
        choice = input("Do you want to add more items to your cart? (yes/no): ").lower()
        if choice != 'yes':
            total_amount = display_cart()
            payment_method = input("Select preferred method of payment (cash/card): ").lower()
            if payment_method == 'cash':
                while True:
                    cash_amount = int(input("Enter the amount you have: "))
                    if cash_amount < total_amount:
                        print("Insufficient amount. Please enter a valid amount.")
                    else:
                        print("Payment successful. Thank you!")
                        break
            elif payment_method == 'card':
                card_number = input("Enter your card number: ")
                card_amount = int(input("Enter the amount in your card: "))
                if card_amount < total_amount:
                    print("Insufficient amount in card. Please select another payment method.")
                    continue
                else:
                    print("Payment successful. Thank you!")
            else:
                print("Invalid payment method. Please select a valid option.")
                continue
            break

if __name__ == "__main__":
    main()