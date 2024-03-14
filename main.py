from manager import *
def main():
    
    object = Manager()

    while True:

        op = input("""
                    1.   Create computer.
                    2.   Present computer.
                    3.   Change the computer OS.
                    4.   Show a list of peripheral.
                    5.   Present all the computers.
                    6.   Add more peripherals to a computer.
                    7.   Exit.
                    Option: """)
        
        if op == "1":
            object.create_computer()
        elif op == "2":
            object.present_computer()
        elif op == "3":
            object.change_os()
        elif op == "4":
            object.show_per()
        elif op == "5":
            object.show_all_computer()
        elif op == "6":
            object.add_peripherals()
        elif op == "7":
            break
        else:
            print("Invalid value, try again")

if __name__ == "__main__":
    main()