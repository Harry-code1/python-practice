phone_power = False


def power_on(phone_power):
    correct_pass = 1046
    passcode = 0
    while passcode != correct_pass:
        passcode = int(input("Enter your passcode: "))
        if passcode.is_integer():
            if passcode != correct_pass:
                print("Incorrect passcode please try again.")



def command_list():
    print("""
    Here is a list of supported commands:
    /commands - Lists the available commands
    /poweroff - Used to turn the phone off
    /calculator - Enters the calculator application
    /bank - Enters the banking application
    /games - Enters the game page 
    /help - Gives information about how things work
    /shutdown
    """)




while True:
    command = input("> ").lower()
    if phone_power == False:
        print("Your phone is off please type /power to turn it on.")
        if command == "/power" and phone_power == False:
            power_on(phone_power)
            phone_power = True
            print("Welcome to your phone. Type /commands for all related actions you can preform.")


        while phone_power == True:
            cmd = input("> ").lower()

            if cmd == "/commands":
                command_list()

            elif cmd == "/poweroff":
                phone_power = False
                print("Your phone has been powered off.")
                break

            elif cmd == "/shutdwown":
