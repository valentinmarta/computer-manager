from computer import *

class Manager:

    brand_list = ['dell','hp','apple']
    os_list = ['mac','linux','windows']

    def __init__(self):
        self.computer_list : list[Computer] = []

    def computer_type(self):
        
        list = []

        while True:
            for pc in Computer.__subclasses__():
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

            per = input("Type a peripheral to add to the computer (exit to finish): ").lower().strip()

            if per == "exit":

                if not list:
                    print("You have to add at least one peripheral.")
                else:
                    return list
            elif not per:
                print("You have to write something, please try again.")
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

    def check_id(self):

        while True:

            flag = True

            try:
                id = int(input("Type the id of the computer: "))
            except Exception as e:
                print(f"Error: {e}")
                flag = False

            for pc in self.computer_list:
                if id == pc.id:
                    print("This id already exist, please try again.")
                    flag = False

            if flag:
                return id

    #first option
    def create_computer(self):
        type = self.computer_type()
        id = self.check_id()
        peripheral_list = self.peripherals()
        os = self.os()
        brand = self.brand()

        if type == "Notebook":
            while True:
                try:
                    weight = int(input("Type the weight of the computer: "))
                    break
                except Exception as e:
                    print(f"Error: {e}")

            pc = Notebook(id, peripheral_list, os, brand, weight)
        elif type == "Desktop":
            while True:
                try:
                    number_cables = int(input("Type the number of cables that needs the computer: "))
                    break
                except Exception as e:
                    print(f"Error: {e}")

            pc = Desktop(id, peripheral_list, os, brand, number_cables)

        self.computer_list.append(pc)
            

    #second option
    def present_computer(self):
                
        if not self.computer_list:
            print("The computer list is empty. First create a computer")
            return

        while True:
            try:
                id = int(input("Type the id of the computer you want to present: "))
                break
            except Exception as e:
                print(f"Error: {e}")

        for pc in self.computer_list:
            if id == pc.id:
                type = pc.return_type()
                pc.present_type()
                pc.present()
                if type == "Notebook":
                    pc.present_n()
                elif type == "Desktop":
                    pc.present_d()
                return
            
        print("That id doesn't exist.")


    #third option
    def change_os(self):
        if not self.computer_list:
            print("The list is empty. First create a computer")
            return
        
        while True:
                
            flag = True

            try:
                id = int(input("Type the id of the computer: "))
            except Exception as e:
                print(f"Error: {e}")
                flag = False

            for pc in self.computer_list:
                if id == pc.id:
                    new_os = self.os()
                    pc.change_os(new_os)
                    return
                
            if flag:
                print("That id doesn't exist. Please try again.")

    #fourth option
    def show_per(self):
        
        if not self.computer_list:
            print("The list is empty. First create a computer.")
            return
        
        while True:

            flag = True

            try:
                id = int(input("Type the id of the computer: "))
            except Exception as e:
                print(f"Error: {e}")
                flag = False

            for pc in self.computer_list:
                if id == pc.id:
                    for per in pc.peripheral_list:
                        print(per, end = " ")

                    return
                
            if flag:
                print("That id doesn't exist. Please try again.")

    #fifth option
    def show_all_computer(self):

        for pc in self.computer_list:

            type = pc.return_type()
            pc.present_type()
            pc.present()

            if type == "Notebook":
                pc.present_n()
            elif type == "Desktop":
                pc.present_d()
            
            print("\n")

    #sixth option
    def add_peripherals(self):

        while True:

            flag = True

            try:
                id = int(input("Type the id of the computer: "))
            except Exception as e:
                print(f"Error: {e}")
                flag = False

            for pc in self.computer_list:
                if id == pc.id:

                    while True:
                        per = input("Type the peripheral you want to add to the computer (exit to finish): ").lower().strip()

                        if per == "exit":
                            return
                        elif not per:
                            print("You have to write something, please try again.")
                        else:
                            pc.peripheral_list.append(per)

            if flag:
                print("That id doesn't exist. Please try again.")