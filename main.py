from manager import *
def main():
    
    object = Manager()

    while True:

        op = input("""
                    1.   Create computer.
                    2.   Present computer.
                    3.   Change the computer OS.
                    4.   Show a list of peripheral.
                    5.   Exit.
                    option: """)
        
        if op == "1":
            object.create_computer()
        elif op == "2":
            object.present_computer()
        elif op == "3":
            object.change_os()
        elif op == "4":
            pass
        elif op == "5":
            break
        else:
            print("invalid value, try again")

if __name__ == "__main__":
    main()