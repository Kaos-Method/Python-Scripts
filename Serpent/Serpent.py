#!/usr/bin/env python3





""" Serpent



    Usage:

           Serpent.py     Author - Kaos Method

           Serpent.py     (-v --version) Version 1.0

           Serpent.py     (-h --help)



    Options:

          -h --help       "Serpent" is a SSH  Botnet  programm,  designed  by  and for Security

                           Proffesionals. "Serpent" is  designed in  Python (Python 3.5.3+, and

                           will continue to stay current). "Serpent"  was also designed  to  be

                           powerful  but  also  minimalistic.  The  program  is rather straight

                           forward.  If  you are in need of actual help, you can contact me, or

                           you can read through the source code to have a better understanding.



          -v --version     Serpent.py 1.0



"""



print ('_________________________________________________________________________________________')

print ('[.......................................................................................]')

print ('[.......................................................................................]')

print ('[..............................::~:~:::..........,:::::~,...............................]')

print ('[...........................:~:~~:~~:=:,::~=,~:,=,~,:~::~==,............................]')

print ('[..........................==,:.,~+II==::,::,~:,+~=,=?,.::,,::,,........................]')

print ('[.........................,,:,~~?,=+::=~,~:=,:+~:=?~::+,+,~~,,,::,,,....................]')

print ('[........................~~~.:~::,==I~:::,::,,.~~~,,:~:=+,,,~.,:,,:,,,:.................]')

print ('[......................:,,,:,.=+=~,....:,::~,,:,~=:.::~==,,.,,,,,,:::,:,,...............]')

print ('[.....................:,,.:,~.,::,=:,,:,:==+,?=,::,:,:,.,,,.:,,,:,::::,,,,,.............]')

print ('[....................:,,:,...,,,:.,:~.+~:,,=+..,,~~,,,.:,~:.:,,,,,:,,~,,,,,,............]')

print ('[...................,,.:.::,,,~,.,,~,+7=~~~:,~~=,,?+,=.,:.:::,,,,::,,,:,,,,.,...........]')

print ('[..................,.....,.,.:.~,,.::II:.......,.:II?:::.:,,::,,,:,.,,,:,,,..,..........]')

print ('[..................:,....,,,~,~,...~:II....,..,..:I??,,,~,,,.,,,,.,,,.,,,...............]')

print ('[.....................,,,:,:~...:.,::7~,,,.,..,.,:7++.:.,.:..,,,,,.......,..............]')

print ('[....................,,,,.,+~::,:,,.:7~.........,:7~.,,,===:,,.,.,.,,....,..............]')

print ('[..................,,:.,,,::=~~,:,:.~I.,........,,7.,,:=:+,,.,,,,...,,...,..............]')

print ('[..................,,,,,,~::,+::~::.=I,,,.......,:I.,,~=??.,........,,...,..............]')

print ('[...................,,.::~:,,:+,~::,.7,,,,,,.,,,,~.,,:?=..,,.....,,.....................]')

print ('[.....................,::,,,,,,,~~,..I:,,,,,,,,,,~.:,~=...,....,...,.,..,...............]')

print ('[......................,,::::,.+.~:,,+:,,,.,,,,,,=,,,+=.,...,...,..,,...,...............]')

print ('[........................,.,,..+:~~,:=:::,.,,,,,,+:::+?,,.,,,.,,,,,,,.,,................]')

print ('[..........................,....=,:,:I:::,.,,::,:?:7:+,,,:::,::,,:,,,,,.................]')

print ('[...............................,.~,:,:::,,,,::,:=~7~?.,.,,,,::,,,,,,,..................]')

print ('[................................~::=~:::,,,::::+I~I==...,,,,,..........................]')

print ('[................................:,~:::::,,,:~:=??+I:...................................]')

print ('[.................................,+:+~:::,,~~+II??~:...................................]')

print ('[.................................,??=+~~:?I=I=7I+I7....................................]')

print ('[..................................~7~+II:I+?I?II+:,....................................]')

print ('[...................................:7+?I,=::?I?I+~.....................................]')

print ('[....................................?I+I:~,?7I?7?......................................]')

print ('[.....................................~I=~~,~=II+,......................................]')

print ('[......................................=+~II:1+.........................................]')

print ('[......................................,.~.,::..........................................]')

print ('[.......................................................................................]')

print ('[.......................................................................................]')

print ('[_______________________________________________________________________________________]')



print ('________________________________________________________________________________________ ')

print ('[  _______    _______    _______    _______    _______    _______    _         _________]')

print ('[ (  ____ \  (  ____ \  (  ____ )  (  ____ \  (  ____ )  (  ____ \  ( (    /|  \__   __/]')

print ('[ | (    \/  | (    \/  | (    )|  | (    \/  | (    )|  | (    \/  |  \  ( |     ) (   ]')

print ('[ | (_____   | (__      | (____)|  | (__      | (____)|  | (__      |   \ | |     | |   ]')

print ('[ (_____  )  |  __)     |     __)  |  __)     |  _____)  |  __)     | (\ \) |     | |   ]')

print ('[       ) |  | (        | (\ (     | (        | (        | (        | | \   |     | |   ]')

print ('[ /\____) |  | (____/\  | ) \ \__  | (____/\  | )        | (____/\  | )  \  |     | |   ]')

print ('[ \_______)  (_______/  |/   \__/  (_______/  |/         (_______/  |/    )_)     )_(   ]')

print ('[_______________________________________________________________________________________]')





from pexpect import pxssh

from docopt import docopt

from getpass import getpass

from colorama import Fore, Style, init





class Client: # Creating "Client" as a class.This class is a wrapper.

    def __init__(self, host, user, password): # Defiing the initializer, while taking four arguements.

        self.host = host

        self.user = user

        self.password = password

        self.session = self.connect()



    def connect(self):

        try:

            options = {'StrictHostKeyChecking': 'no', 'UserKnownHostsFile': '/dev/null'}

            s = pxssh.pxssh(echo = False, options = options) # The lowercase letter "s" is  assigned as a class variable for the "pxssh" module.

            s.login(self.host, self.user, self.password) # Calling the method "s.login".



            return s

        except Exception as e:

            print (Fore.RED + '[-] Connection Failed' + Fore.RESET)

            print (e)

            anykey = input('')

        exit

        mainMenu()



    def send_command(self, cmd): # Defining the "send_command".

        self.session.sendline(cmd)

        self.session.prompt()

        return self.session.before



def ssh__command(command, ssh): # Defineing the "ssh" command (botnet command).

    for client in ssh: # The commands are executed for "client in ssh" (botnet).

        output = client.send_command(command)

        print (Fore.GREEN + '[*] Output from ' + client.host + Fore.RESET)

        print ('[+] ' + output + '\n')



def add_client(host, user, password, botnet): # Defining function to allow "client" to be added.

    client = Client(host, user, password)

    botnet.append(client)



def main():

    g = getpass # I'm using the "Getpass" module to prevent any of the following user inputs from being Echoed.

    ip = g(prompt=Style.DIM + 'SRP Shell:') # This is where the I"P address" is entered.

    host = g(prompt=Style.DIM + 'SRP Shell:') # This is where the "host" is entered.

    psw  = g(prompt=Style.DIM + 'SRP Shell:' ) # This is where the "Password" is entered.

    sshcmd = g(prompt=Style.DIM + 'SRP Shell:') # This is where the botnet commands are entered.

    botnet = []



    add_client('ip', 'host', 'psw', botnet)

    ssh__command('sshcmd', botnet)





def SRP_Shell(): # Defining "SRP Shell". This allows the SRP Shell to be used directly to execute commands remotely.

    g = getpass # Variable for the getpass module.

    try:

        while True:



            ssh_cmd = g(prompt=Style.DIM + 'SRP Shell:') # This is the SRP Shell, protected from Echo by getpass.

            print ()

    except KeyboardInterrupt: # Except KeyInterrupt as the method to get to the main menu.

        pass # The pass statement is used to pass anything that isn't the KeyboardInterrupt. Allowing the SRP Shell to be used as long as needed.



    mainMenu()



def Options_Menu(): # Defining a function to create the menu driven interface.

    print ()

    print (Style.DIM + 'Available Commands')

    print ('==================')

    print ()

    print (Style.DIM + 'Commands                    Description')

    print ('--------                    ------------')

    print ()

    print (Style.DIM + 'Commands                    list of commands')

    print (Style.DIM + 'User Agreement              The User Agreement')

    print (Style.DIM + 'Main Menu                   Back to Main Menu')

    print (Style.DIM + 'Exit                        Exits the program')



    g = getpass



    while True: # A While loop to control the menu driven interface.

        try:

            print ()

            selection = str(g(prompt = Style.DIM + 'SRP Shell:'))

            print ()

            if selection == 'Commands':

                Commands()

                print()

                break

            elif selection == 'User Agreement':

                User_Agreement()

                break

            elif selection == 'Main Menu':

                mainMenu()

                break

            elif selection == 'Exit':

                break

            Options_Menu()

        except ValueError:

            print (Fore.RED + 'Error' + Fore.RESET)



    exit

    mainMenu()



def Commands(): # Defining a function to create the menu driven interface.

    print ()

    print (Style.DIM + 'Available Commands')

    print ('==================')

    print ()

    print (Style.DIM + 'Commands                     Description')

    print ('--------                     -----------')

    print ()

    print (Style.DIM + 'SRP Shell                    Command to initiate SRP Shell')

    print (Style.DIM + '-x                           Command to initiate SRP Shell')

    print (Style.DIM + 'Sysinfo                      DisplaYS system info of clients in Serpent (Botnet)')

    print (Style.DIM + 'sys                          Displays system info of clients in Serpent (Botnet)')

    print (Style.DIM + 'Add Client                   Adds client to Serpent (Botnet)')

    print (Style.DIM + '-a                           Adds client to Serpent (Botnet)')

    print (Style.DIM + 'Manage Clients               Manage clients in Serpent (Botnet)')

    print (Style.DIM + '-m                           Manage clients in Serpent (Botnet)')

    print (Style.DIM + 'Interact                     Interacts with one/all clients')

    print (Style.DIM + '-i                           Interacts with one/all clients')

    print (Style.DIM + 'Exit                         Exits the current Menu, or the Program')





    g = getpass



    while True: # A While loop to control the menu driven interface.

        try:

            print ()

            selection = str(g(prompt = Style.DIM + 'SRP Shell:'))

            print ()

            if selection == 'SRP Shell':

                SRP_Shell()

                print()

                break

            elif selection == '-x':

                SRP_Shell()

                break

            elif selection == 'Sysinfo':

                Sysinfo()

                break

            elif selection == 'sys':

                Sysinfo()

                break

            elif selection == 'Add Client':

                main()

                break

            elif selection == '-a':

                main()

                break

            elif selection == 'Manage Clients':

                ManageClient()

                break

            elif selection == '-m':

                ManageClient()

                break

            elif selection == 'Interact':

                Interact()

                break

            elif selection == '-i':

                Interact()

                break

            elif selection == 'Exit':

                break

        except ValueError:

            print (Fore.RED + 'Error' + Fore.RESET)

    exit

    mainMenu()



def mainMenu(): # Defining a function to create the menu driven interface.

    print ()

    print (Style.DIM + 'Available Commands')

    print ('==================')

    print ()

    print (Style.DIM + 'Commands                     Description')

    print ('--------                     -----------')

    print ()

    print (Style.DIM + 'Add Client                   adds client to Serpent (Botnet)')

    print (Style.DIM + 'Manage Clients               manage clients in Serpent (Botnet)')

    print (Style.DIM + 'Options                      option\'s menu')

    print (Style.DIM + 'SRP Shell                    Serpent Shell, to execute commands')

    print (Style.DIM + 'Interact                     interacts with one/all clients')

    print (Style.DIM + 'List                         lists all clients within Serpent (database)')

    print (Style.DIM + 'Sysinfo                      displays system info of clients in Serpent (Botnet)')

    print (Style.DIM + 'Exit                         exits the system')

    print ()



    g = getpass



    while True: # A While loop to control the menu driven interface.

        try:

            selection=str(g(prompt = Style.DIM + 'SRP Shell:'))

            print ()

            if selection == "Add Client":

                main()

                print ()

                break

            elif selection == 'Manage Clients':

                ManageClient()

                break

            elif selection == 'Options':

                Options_Menu()

                break

            elif selection == 'SRP Shell':

                SRP_Shell()

                break

            elif selection == '-x':

                SRP_Shell()

                break

            elif selection == 'Interact':

                Interact()

                break

            elif selection == 'list':

                Lists()

                break

            elif selection == 'Sysinfo':

                Sysinfo()

                break

            elif selection == 'Exit':

                break

        except ValueError:

            print (Fore.RED + 'Error' + Fore.RESET)

    exit



mainMenu()



if __name__ == '__main__':



    init()

    docopt(__doc__, version = Style.DIM + 'Serpent.py VER.-1.0')

    main()
