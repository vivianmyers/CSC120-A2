"""Class Computer creates Computer objects with all relevant information"""
class Computer:

    # What attributes will it need?
    description: str 
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """Constructor: Assigns relevant attributes values"""
    def __init__(self, description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int, 
                 memory: int, 
                 operating_system: str, 
                 year_made: int,
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    # What methods will you need?

    """This method tells ResaleShop how to print the descruption of a Computer object"""
    def __str__(self) -> str:
        return f'Description: {self.description}, Processor_type: {self.processor_type}, hard_drive_capacity: {self.hard_drive_capacity}, memory: {self.memory}, operating_system: {self.operating_system}, year_made: {self.year_made}, price: {self.price}'

    """Helper method to update the price of a Computer Object"""
    def set_price(self, new_price: int) -> None:
        self.price = new_price

    
"""Main method for testing only"""
def main():
    my_computer1 : Computer = Computer("Macbook Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
    #print("Description:", my_computer.description)

main()