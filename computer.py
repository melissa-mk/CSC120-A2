class Computer:

    # What attributes will it need?
    description:str
    processor_type:str
    hard_drive_capacity:int
    memory:int
    os:str
    year_made:int
    price:int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, os, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.os = os
        self.year_made = year_made
        self.price = price

    # How will you convert the object to a string for printing?
    def to_string(self):
        return f"Description: {self.description}, Processor: {self.processor_type}, Hard Drive Capacity: {self.hard_drive_capacity}GB, Memory: {self.memory}GB, Operating System: {self.os}, Year Made: {self.year_made}, Price: ${self.price}"
    
    # What methods will you need?
    def update_price(self, new_price: int):
        self.price = new_price

    def update_os(self, new_os: str):
        self.os = new_os
    
        
def main():
    computer:Computer=Computer(
        "Mac Pro",
        "M3",
        256,
        32,
        "MacOS Sonoma",
        2023,
        1099
    )
    print(computer.to_string())
    print("Do you want to update the price? (y/n)")
    choice = input()
    if choice == 'y':
        print("Enter new price:")
        new_price = float(input())
        computer.update_price(new_price)
        print(f"Price updated to {new_price}")

if __name__=="__main__":
    main()
