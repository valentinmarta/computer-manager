class Computer:
    
    def __init__(self, id, peripheral_list, os, brand):
        
        self.id = id
        self.peripheral_list = peripheral_list
        self.os = os
        self.brand = brand

    def present(self):
        print(f"Computer id: {self.id}, OS: {self.os}, Computer brand: {self.brand}, List of peripherals: {self.peripheral_list}")

    def present_type(self):
        print(f"The computer type is: {type(self).__name__}")

    def return_type(self):
        # it returns the type to use it on the presentation of other computers
        return type(self).__name__

    def change_os(self, new_os):
        self.os = new_os

class Desktop(Computer):

    def __init__(self, id, peripheral_list, os, brand, number_cables):

        super().__init__(id, peripheral_list, os, brand)
        self.number_cables = number_cables

    def present_d(self):
        print(f"Number of cables: {self.number_cables}")

class Notebook(Computer):

    def __init__(self, id, peripheral_list, os, brand, weight):

        super().__init__(id, peripheral_list, os, brand)
        self.weight = weight

    def present_n(self):
        print(f"computer weight: {self.weight}")