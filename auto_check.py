import os

def os_kernel_check():
    if flag != 0:
        print("\x1b[33m                                          os/kernel check function\x1b[0m")
        print("")
        os.system('uname -a')
        os.system('cat /etc/os-release')
        #os.system('cat /etc/issue')
        print("----------------------------------------------------------------------------------------------------------------------------------")
        root_check()

    else:
        print("os/kernel check function")
        os.system('uname -a')
        os.system('cat /etc/os-release')
        os.system('cat /etc/issue')
        

def network_info():
    try:
        os.system('cmd /k "ipconfig"')
    except:
        print("Invalid command")

def root_check():
    if flag != 0:
        print("\x1b[33m                                          Root Service Check Function\x1b[0m")
        print("")
        os.system('ps aux | grep root')
        print("----------------------------------------------------------------------------------------------------------------------------------")
        SUID_GUID_check()

    else:
        #os.system('clear')
        print("root service check function")
        os.system('ps aux | grep root')
        
def SUID_GUID_check():
    if flag != 0:
        print("\x1b[33m                                              SUID/GUID Check\x1b[0m")
        print("")
        print("SUID Check")
        print("")
        os.system('find / -perm -u=s -type f 2>/dev/null')
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("GUID Check")
        print("")
        os.system('find / -perm -g=s -type f 2>/dev/null')
        #print("----------------------------------------------------------------------------------------------------------------------------------")
        
    else:
        #os.system('clear')
        print("SUID Check")
        print("")
        os.system('find / -perm -u=s -type f 2>/dev/null')
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("GUID Check")
        print("")
        os.system('find / -perm -g=s -type f 2>/dev/null')
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("SUID/GUID binaries check function")
        

def Sudoer_Permission_Check():
    try:
        print("\x1b[33m                                          Sudoer_Permission_Check\x1b[0m")
        os.system('sudo -l')
        #print("----------------------------------------------------------------------------------------------------------------------------------")

    except:
        print("You don't have sudoer permission")
        

def Cronjobs():
        print("\x1b[33m                                          Cronjobs\x1b[0m")
        os.system('cat /etc/crontab')

def Improper_permission_check():
    print("Improper_permission_check")
    os.system('ls -l /etc | grep shadow')
    
def passwords_keys_historyfiles():
    print("Check pass keys")
    os.system('cat ~/.*history | less')

def main():
    print("=" * 180)
    print("\x1b[34;9;3m                                            .*############*.                   ")                                            
    print("                                          :##################-                 ")                                            
    print("                                         *####################*                ")                                            
    print("                                        *######################*               ")                                            
    print("                                       =########################=              ")                                            
    print("                                      -##########################=             ")                                            
    print("                                     .############################.            ")                                            
    print("                                     *#############################            ")                                            
    print("                                    +##############################+           ")                                            
    print("                                  .-++++++++++++++++++++++++++++++++-.         ")                                            
    print("                              -*###==================================*###-     ")                                            
    print("                            +############***********************###########+   ")                                            
    print("                           +################################################+  ")                                            
    print("                            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#   ")                                            
    print("                                 =@@@:::-----#@@+===========----:::@@@=        ")                                            
    print("                                  @@@-:::-@-.:--..%+:::=%%%**=:::::@@@         ")                                            
    print("                              .:--%@@-::+-.......  .@---:::::::::::%@%--:.     ")                                            
    print("                             .----#@@-:-@...=%%#....:*::@@@#:::::::%@#----.    ")                                            
    print("                             :---==%@-:=*...*@@%.....#::@@@@:::::::%%==---:    ")                                            
    print("                              -==--*@-:-@...........*=:::-:::::::::@#--=--     ")                                            
    print("                              :---==%-::-@........ #=:=+-::::::::::%==---:     ")                                            
    print("                               :---==-::::-@*:::+@@%%@@@@@#::::::::===-=:      ")                                            
    print("                                .=----:-::=%@@@@@@#::+@@@@@@%=::-::----.       ")                                            
    print("                               :##+=--:*@@@@@@%*::::--:*%@@@@@@@*:-==+##:      ")                                            
    print("                             =#######=::-+*#*-:::::::--:::=+**+-::=#######=    ")                                            
    print("                           :#########=-::::::::::::----::::::::::-=#########:  ")                                            
    print("                           *##########==*=:::::::-----::::::::::-=##########*  ")                                            
    print("                              *###########*=-:::---::::::::::----*########.    ")                                            
    print("                                +############*+==-::::::::-=---+#######+       ")                                            
    print("                                :############%%%*------------:#######*         ")                                            
    print("                              .############%%%%+--------:.    #########.       ")                                            
    print("                             *############%%%%: +%@@@@%+      #####%####+      ")                                            
    print("                            *############%%%%. .@@@@@@@@:    -####%######*     ")                                            
    print("                           *###########%%%%%#.  @@@@@@@@  .#*####%%#######+    ")                                            
    print("                          :##########%%%%%####  @@@@@@@@. ######%%#########    ")                                            
    print("                          :########%%%%%%#####+:@@@@@@@@-+#####%%##########.   ")                                            
    print("                           *#####%%%%%##%%#####%@@@@@@@@%#####%%###########    ")                                            
    print("                            +%%%%#+.#####%%%####@@@@@@@@####%%%###########+    ")                                            
    print("                                   .#######%%####@@@@@@####%%############*     ")                                            
    print("                                   :########%%%###@@@@###%%%############*      ")                                            
    print("                                   +#########%%%%#%@@%##%%%############*       ")                                            
    print("                                   ###########%%%%%%%#%%%%###########%*        ")                                            
    print("                                  :#############%%%##%%%#############+         ")                                            
    print("                                  +#################%################*         ")                                            
    print("                                  ################%%##################=        ")                                            
    print("                                 ################%%####################        ")                                            
    print("                                .###############%%#####################=       ")                                            
    print("                                ################%#%@@@##################.      ")                                            
    print("                               +###############%%#######################*      ")                                            
    print("                              .################%#########################+     ")                                            
    print("                                +##############%#######################*       ")                                            
    print("                                  .+###########%###@@%##############*:         ")                                            
    print("                                       @%######%###############+-.             ")                                            
    print("                                       -@@@@@@@@@@@@@@@@@@@@@@                 ")                                            
    print("                                        @@@@@@@@@@@@@@@@@@@@@+                 ")                                            
    print("                                         @@@@@@@@@@@@@@@@@@@@                  ")                                            
    print("                                         :@@@@@@@@@@@@@@@@@@                   ")                                            
    print("                                          +@@@@@@@@@@@@@@@@                    ")                                            
    print("                                           %@@@@@@@@@@@@@@=                    ")                                            
    print("                                            @@@@@@@@@@@@@+                     ")                                            
    print("                                             @@@@@@@@@@@+                      ")                                            
    print("                                          %@@@@@@@@@@@@@@@@#                   ")                                            
    print("                                        +@%@*@@@@@@@@@@@@@@@@:                 ")                                            
    print("                                        @@@@@@@@@@=*@@@@@@@@@@                 ")
    print("\x1b[31;9;3m/*  _      _                    _____      _       ______  _____  _____     _____                           _               _                     _____        _          */ ")
    print("/* | |    (_)                  |  __ \    (_)     |  ____|/ ____|/ ____|   |_   _|                         | |             (_)                   |  __ \      | |         */ ")
    print("/* | |     _ _ __  _   ___  __ | |__) | __ ___   _| |__  | (___ | |          | |  _ __  ___ _ __   ___  ___| |_ ___  _ __   _ ___    ___  _ __   | |  | |_   _| |_ _   _  */ ")
    print("/* | |    | | '_ \| | | \ \/ / |  ___/ '__| \ \ / /  __|  \___ \| |          | | | '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__| | / __|  / _ \| '_ \  | |  | | | | | __| | | | */ ")
    print("/* | |____| | | | | |_| |>  <  | |   | |  | |\ V /| |____ ____) | |____ _   _| |_| | | \__ \ |_) |  __/ (__| || (_) | |    | \__ \ | (_) | | | | | |__| | |_| | |_| |_| | */ ")
    print("/* |______|_|_| |_|\__,_/_/\_\ |_|   |_|  |_| \_/ |______|_____/ \_____(_) |_____|_| |_|___/ .__/ \___|\___|\__\___/|_|    |_|___/  \___/|_| |_| |_____/ \__,_|\__|\__, | */ ")
    print("/*                                                                                         | |                                                                      __/ | */ ")
    print("/*                                                                                         |_|                                                                     |___/  */ \033[0m") 
    print("=" * 180)
    while True:
        global flag
        flag = 0
        print("<>" * 90)
        print("\x1b[34m                                                                                       MAIN MENU \x1b[0m")
        print("<>" * 90)
        OPTION = int(input("""
		    1. Full Scan
		    2. OS/Kernel Check
		    3. Root Service CheckS
		    4. SUID/GUID Check
		    5. Sudoer Permission Check
		    6. Cronjobs
		    7. EXIT
              Enter Your Choice : """))

        if OPTION == 1:
            print("<>" * 50)
            print("\x1b[34m                                                FULL SCAN \x1b[0m")
            print("<>" * 50)
            flag = flag + 1
            os_kernel_check()
            
        elif OPTION == 2:
            print("<>" * 50)
            print("\x1b[34m                                                OS KERNAL CHECK \x1b[0m")
            print("<>" * 50)
            os_kernel_check()

        elif OPTION == 3:
            print("<>" * 50)
            print("\x1b[34m                                                ROOT SCAN \x1b[0m")
            print("<>" * 50)
            root_check()

        elif OPTION == 4:
            print("<>" * 50)
            print("\x1b[34m                                                SUID/GUID CHECK \x1b[0m")
            print("<>" * 50)
            SUID_GUID_check()

        elif OPTION == 5:
            print("<>" * 50)
            print("\x1b[34m                                                SUDOER PERMISSION CHECK \x1b[0m")
            print("<>" * 50)
            Sudoer_Permission_Check()
            
        elif OPTION == 6:
            print("<>" * 50)
            print("\x1b[34m                                                CRON JOBS \x1b[0m")
            print("<>" * 50)
            Cronjobs()
            
        elif OPTION == 7:
            print("<>" * 90)
            print("\x1b[34m                                                                                       THANK YOU \x1b[0m")
            print("<>" * 90)
            break

        else:
            print("Invalid option. Press ENTER to continue.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
