# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import auto_check.py

def main():
    global flag
    flag =0

    print("This is the main function")  # Press Ctrl+F8 to toggle the breakpoint.
    OPTION = input("""
    1. OS/Kernel Check
    2. Root Service Check
    3. SUID/GUID Check
    4. Full Scan
    5. EXIT
    LPC>>
    """)
    #print("You chose " + OPTION)
    if OPTION == "1":
        #print("You chose option 1")
        os_kernel_check()
    elif OPTION == "2":
        print("You chose option 2")
        root_check()
    elif OPTION == "3":
        print("You chose option 3")
        SUID_GUID_check()
    elif OPTION == "4":
        flag = flag + 1
        os_kernel_check()
    elif OPTION == "5":
        exit()
    else:
        BAD_OPTION = input("Invalid option. Press ENETR to continue.")
        main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #auto_check()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
