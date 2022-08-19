from src.ui import bcolors


class WarningCy:

    def warning(warn: str, routeOfFile=""):
        if warn == "shellMac":
            print(
                f"{bcolors.WARNING}Shell that program needs to know it hasn't been recognized\n {bcolors.ENDC}")
        elif warn == "RouteDoesntExist":
            print(
                f"{bcolors.WARNING}Couldn't find file or directory -> {bcolors.ENDC}" + routeOfFile)
            return
        elif warn == "checkCorrect":
            print(
                f"{bcolors.WARNING}Unexpected input, please select 'y, n or q'{bcolors.ENDC}")
            return
        elif warn == "os":
            print(
                f"{bcolors.WARNING}Your operative system is not compatible with this program{bcolors.ENDC}")
        elif warn == "cacheFolderAlreadyExists":
            print(
                f"{bcolors.WARNING}You already have a cache folder, you'll be prompted to the next question{bcolors.ENDC}")
            return
        elif warn == "varClearingError":
            print(
                f"{bcolors.FAIL}Recognition error of environment variable. Make sure that \nthis environment variable is one of the 5 variables that the program uses.\n Variable that caused the error -> {bcolors.ENDC}" + routeOfFile)
        else:
            print("WARNING NOT RECOGNIZED")
        quit()
