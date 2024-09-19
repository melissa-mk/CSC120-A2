from typing import Dict
from computer import Computer

class ResaleShop:

    # class  attributes 
    inventory: Dict[int, Dict] = {}
    itemID: int = 0 # Item ID that will be incremented for each new addition to the inventory
  
    # class constructor
    def __init__(self):
        self.inventory:Dict[int, Computer]={}
        self.itemID:int=0

    # class methods
    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: Dict):
        self.itemID += 1 # increment the computer's itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, id:int):
        if id in self.inventory:
            del self.inventory[id]
            print(f"Computer {id} sold")
        else:
            print(f"Computer {self.id} does not exist")
   
   # display all computers in stock
    def print_computers(self):
        if self.inventory:
            print(f"Inventory")
            for item_id in self.inventory:
                print(f'Computer ID: {item_id}, Description: {self.inventory[item_id].description}, OS: {self.inventory[item_id].os}, Price: {self.inventory[item_id].price}')
        else:
            print("The inventory is empty.")

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """

def main():
    rs:ResaleShop=ResaleShop()
    computer:Computer=Computer("Mac Pro", "M3", 256, 32, "MacOS Sonoma", 2023, 1099)
    comp:Computer=Computer("Mac Air", "M2", 512, 16, "MacOS Monterey", 2022, 1199)    
    # buy the macbook pro
    rs.buy(computer)
    # buy the macbook air
    rs.buy(comp)
    # show all computers in inventory
    rs.print_computers()    
    # sell the macbook pro
    rs.sell(1)
    print("Enter new price: ")
    new_price: int = input()
    comp.price=new_price
    print("Enter new OS")
    new_os: str=input()
    comp.os=new_os 
    # show current data about computers in inventory
    rs.print_computers()

if __name__=="__main__":
    main()