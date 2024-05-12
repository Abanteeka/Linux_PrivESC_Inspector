import os

# import subprocess
# os.system("ls")
# os.popen("ls").read()
# subprocess.run()
def os_kernel_check():
    # this function will check for os, and kernel info
    if flag != 0:
        print("os/kernel check function")
        os.system('uname -a')
        os.system('cat /etc/os-release')
        #os.system('cat /etc/issue')
        os.system('cls')
        print("-------------------------------------------------")
        root_check()

    else:
        print("os/kernel check function")
        os.system('uname -a')
        os.system('cat /etc/os-release')
        os.system('cat /etc/issue')
        GOTOMAIN = input("Press ENTER to return to MAIN function")
        main()

def network_info():  #later
    try:
        os.system('cmd /k "ipconfig"')
    except:
        print("Invalid command")

# this function will check for services running as root
def root_check():
    if flag != 0:
        print("Root Service Check Function")
        os.system('ps aux | grep root')
        print("-------------------------------------------------")
        SUID_GUID_check()

    else:
        os.system('cls')
        print("root service check function")
        GOTOMAIN = input("Press ENTER to return to MAIN function.")
        main()

# this function will check for abusable SUID/GUID binaries
def SUID_GUID_check():
        if flag != 0:
        print(flag)
        os.system('clear')
        print("SUID/GUID Check")
        print("")
        print("SUID Check")
        os.system('find / -perm -u=s -type f 2>/dev/null')
        print("GUID Check")
        os.system('find / -perm -g=s -type f 2>/dev/null')
        print("-------------------------------------------------")
        GOTOMAIN = input("Full Scan Completed! Press ENTER to return to MAIN function")
        main()
    else:
        os.system('clear')
        # print(flag)
        os.system('find / -perm -u=s -type f 2>/dev/null')
        print("GUID Check")
        os.system('find / -perm -g=s -type f 2>/dev/null')
        print("-------------------------------------------------")
        print("SUID/GUID binaries check function")
        GOTOMAIN = input("Press ENTER to return to MAIN function.")
        main()

def Sudoer_Permission_Check():
    try:
        print("Sudoer_Permission_Check")
        os.system('sudo -l')
        print("-------------------------------------------------")
        GOTOMAIN = input("Full Scan Completed! Press ENTER to return to MAIN function")
    except:
        print("You don't have sudoer permission")
    exit()

def Cronjobs():
        print("Cronjobs")
        os.system('cat /etc/crontab')   #any possible failure

def Improper_permission_check():
    print("Improper_permission_check")
    os.system()
#Main Menu
def main():

    while True:
        global flag
        flag = 0
        print("This is the main function")  # Press Ctrl+F8 to toggle the breakpoint.
        OPTION = input("""
            1. OS/Kernel Check
            2. Root Service Check
            3. SUID/GUID Check
            4. Full Scan
            5. EXIT
            LPC>>
            """)

        if OPTION == "1":
            # print("You chose option 1")
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
            BAD_OPTION = input("Invalid option. Press ENTER to continue.")
            main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #auto_check()
