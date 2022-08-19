from src.osC import OSinteract
from src.mac import MacInterface
from src.ui import bcolors


class App:

    def initApp(varConfig):
        OS = OSinteract.getOS().lower()

        if OS == "darwin":
            MacInterface.initiateConfiguration(varConfig)
            MacInterface.printEnvsConfigMac()

        else:
            print(f"{bcolors.WARNING}Not implemented in OS -> {bcolors.ENDC}" + OS)

        print("\nPress Enter to terminate the program")
        input('')
        OSinteract.exitProgram()
