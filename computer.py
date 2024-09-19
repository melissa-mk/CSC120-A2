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

    # What methods will you need?