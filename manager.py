from computer import *

class Manager:

    brand_list = ['dell','hp','apple']
    os_list = ['mac','linux','windows']

    def __init__(self):
        self.computer_list : list[Computer] = []

    def computer_type(self):
        
        list = []

        while True:
            for pc in Computer.__subclasses__:
                print(pc.__name__)
                list.append(pc.__name__)

            pc = input("Select one type of computer: ").lower().capitalize()

            if pc in list:
                return pc
            else:
                print("That computer type doesn't exist, please try again.")

    
    def peripherals(self):
        list = []

        while True:

            per = input("type a peripheral to add to the computer (exit to finish): ").lower()

            if not list:
                print("you have to add at least one peripheral.")
            elif per == "exit":
                return list
            else:
                list.append(per)

    def os(self):

        while True:
            for os in self.os_list:
                print(os)

            os = input("Select one OS: ").lower()

            if os in self.os_list:
                return os
            else:
                print("That OS is not available, please try again.")

    def brand(self):
        
        while True:
            for brand in self.brand_list:
                print(brand)

            br = input("Select one brand: ").lower()

            if br in self.brand_list:
                return br
            else:
                print("That brand is not available, please try again.")

    #first option
    def create_computer(self):
        type = self.computer_type()
        id = input("Type the id of the computer: ") 
        peripheral_list = self.peripherals()
        os = self.os(self)
        brand = self.brand(self)

        if type == "Notebook":
            while True:
                try:
                    weight = input("Type the weight of the computer: ")
                    break
                except Exception as e:
                    print(f"Error: {e}")

            pc = Notebook(id, peripheral_list, os, brand, weight)
        elif type == "Desktop":
            while True:
                try:
                    number_cables = input("Type the number of cables that needs the computer: ")
                    break
                except Exception as e:
                    print(f"Error: {e}")

            pc = Desktop(id, peripheral_list, os, brand, number_cables)
            

    #second option
    def present_computer(self):
        pass

    #third option
    def change_os(self):
        pass

    #fourth option
    def show_per(self):
        pass