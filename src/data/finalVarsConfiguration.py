from src.ui import bcolors
from src.data.validEnvironmentVariables import EnvironmentVariables


class FinalConfiguration:

    def getEnvironmentVariables():
        return EnvironmentVariables.getEnvironmentVariables()

    def printData():
        envVars = FinalConfiguration.getEnvironmentVariables()

        print(
            f"{bcolors.HEADER}\n\n Configured environment variables: {bcolors.ENDC}")
        print("-----------------------------------" + "\n")
        for key in envVars.keys():
            print(key + " -> " +
                  str(FinalConfiguration.getEnvironmentVariables()[key]))

    def printEnvConfig():
        envVars = FinalConfiguration.getEnvironmentVariables()

        for key in envVars.keys():
            if not envVars[key]:
                envVars[key] = f"{bcolors.FAIL}" + \
                    "Not configured" + f"{bcolors.ENDC}" + "\n"
            else:
                envVars[key] = f"{bcolors.OKCYAN}" + \
                    envVars[key] + f"{bcolors.ENDC}" + "\n"

        FinalConfiguration.printData()
