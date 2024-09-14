from typing import Dict, Optional
from computer import Computer

"""Class ResaleShop handles objects of type Computer and methods to modify inventory and computers"""
class ResaleShop:

    # What attributes will it need?
    inventory: Dict[int, Computer] 
    itemID: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """Constructor"""
    def __init__(self):
        self.inventory : Dict[int, Computer] = {}


    # What methods will you need?

    """Takes a Computer object containing all information about a computer, adds it to inventory,
    and returns the assigned itemID"""
    def buy(self, computer: Computer):
        global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
    
    """Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory through the set_price() method, prints error message otherwise"""
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].set_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    

    """Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise"""
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """Prints all the items in the inventory (if it isn't empty), prints error otherwise"""
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for item_id in self.inventory:
            # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")


    """Takes an itemID and new OS. If the itemID exists, it changes the computers price based on the year_made.
    Prints error otherwise."""
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.set_price(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.set_price(250)  # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.set_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.set_price(1000) # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")   


"""main method for testing purposes"""
def main():
    shop = ResaleShop()
    my_computer = Computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
    
    my_computer2 = Computer("Windows Dell XPS",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "Windows 10", 2013, 1500)

    shop.buy(my_computer)
    shop.print_inventory()

    shop.buy(my_computer2)
    shop.print_inventory()

    shop.update_price(1, 10000)
    shop.print_inventory()

    shop.update_price(5, 10000)

    print("-------------------------------------------------------")
    shop.refurbish(2, "Windows11")
    shop.print_inventory()

    shop.sell(1)
    shop.print_inventory()

    

main()