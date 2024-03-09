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

