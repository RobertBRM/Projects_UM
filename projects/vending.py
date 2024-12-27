
class VendingMachine:

    def __init__(self):
        self.inventory = []
        self.balance = 0.0
        self.total_sales = []

    #Test: Passed
    def add_item(self, name, price, quantity):
        for item in self.inventory:
            if item["Name"] == name:
                item["Price"] = price
                item["Quantity"] += quantity
                print(f"{quantity} {name}(s) added to inventory")
                return
        self.inventory.append({"Name" : name, "Price" : price, "Quantity" : quantity})
        print(f"{quantity} {name}(s) added to inventory")
        return None

    #Test: Passed
    def get_item_price(self, name):
        for item in self.inventory:
            if item["Name"] == name:
                return item["Price"]
        print("Invalid item")
        return None

    #Test: Passed     
    def get_item_quantity(self, name):
        for item in self.inventory:
            if item['Name'] == name:
                return item['Quantity']
        print('Invalid item')
        return None
    
    #Test: Passed
    def list_items(self):
        sorted_inventory = sorted(self.inventory, key=lambda x: x["Name"])
        if not self.inventory:
            print('No items in the vending machine')
            return None
        else:
            print("Available items:")
            for item in sorted_inventory:
                print(f'{item["Name"]} (${item["Price"]}): {item["Quantity"]} available')
    
    #Test: Passed   
    def insert_money(self , dollar_amount):
        if dollar_amount in (1.0,2.0,5.0):
            self.balance += dollar_amount
            self.balance = round(self.balance, 2)
            print(f'Balance: {self.balance}')
        else:
            print('Invalid amount')
        

    #Test: Passed
    def purchase(self, name):
        for item in self.inventory:
            if item['Name'] == name:
                if item['Price'] > self.balance:
                    print(f"Insufficient balance. Price of {item['Name']} is {round(item['Price'],2)}")
                    return
                elif item['Quantity'] == 0:
                    print(f"Sorry, {item['Name']} is out of stock")
                    return
                else:                                
                    self.balance -= round(item['Price'] , 2)
                    self.balance = round(self.balance, 2)
                    self.total_sales.append({
                        "Name" : item['Name'],
                        "Price" : round(item['Price'] , 2)
                        })
                    item['Quantity'] -= 1
                    print(f"Purchased {item['Name']}\nBalance: {round(self.balance,2)}")
                    return
        print("Invalid item")
        return None

    #Test: Passed
    def output_change(self):
        if self.balance == 0:
            print('No change')
            return None
        else:
            print(f'Change: {self.balance}')
            self.balance = 0.0
            return None

    #Test: Passed
    def remove_item(self, name):
        for item in self.inventory:
            if item['Name'] == name:
                self.inventory.remove(item)
                print(f"{item['Name']} removed from inventory")
                return
        print("Invalid item")
        return None

    #Test: Passed
    def empty_inventory(self):
        self.inventory.clear()
        print('Inventory cleared')

    #Test: Passed
    def get_total_sales(self):
        total = 0
        for sale in self.total_sales:
            total += sale['Price']
        return round(total,2)

    def stats(self, n):
        if not self.total_sales:
            print("No sale history in the vending machine")
            return
        recent_sales = self.total_sales[-n:]
        stats = {}
        for sale in recent_sales:
            if sale['Name'] not in stats:
                stats[sale['Name']] = {"total_sales": 0, "total_quantity": 0}
            stats[sale['Name']]["total_sales"] += sale['Price']
            stats[sale['Name']]["total_quantity"] += 1
        print(f"Sale history for the most recent {len(recent_sales)} purchase(s):")
        for name, data in sorted(stats.items()):
            total_sales = data['total_sales']
            if total_sales == round(total_sales, 1):
                formatted_sales = f"{total_sales:.1f}"
            else:
                formatted_sales = f"{total_sales:.2f}"
            print(f"{name}: ${formatted_sales} for {data['total_quantity']} purchase(s)")

vm = VendingMachine()
vm.add_item("Qfdmkx", 6.05, 8)
vm.add_item("Sztqqgu", 2.57, 7)
vm.add_item("Fuzhtwr", 5.03, 7)
vm.insert_money(5.00)
vm.insert_money(2.00)
vm.purchase("Qfdmkx")
vm.insert_money(2.00)
vm.purchase("Sztqqgu")
vm.insert_money(5.00)
vm.insert_money(1.00)
vm.purchase("Qfdmkx")
vm.purchase("Qfdmkx")
print(vm.get_total_sales())