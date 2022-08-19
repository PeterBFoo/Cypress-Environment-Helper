from src.ui import bcolors
from src.data.validEnvironmentVariables import EnvironmentVariables


class InitialConfiguration:

    def getEnvironmentVariables():
        return EnvironmentVariables.getEnvironmentVariables()

    def setVariableConf(var, value):
        envVars = InitialConfiguration.getEnvironmentVariables()
        envVars[var] = value

    def clearVariablesConf():
        envVars = InitialConfiguration.getEnvironmentVariables()
        varsToClear = list(filter(lambda k: k != "", envVars))
        
        for key in varsToClear:
            envVars[key] = ""
        
    def printData():
        envVars = InitialConfiguration.getEnvironmentVariables()
        print(
            f"{bcolors.OKGREEN}\n\n Configuration preview: {bcolors.ENDC}")
        print("------------------------" + "\n")
        for key in envVars.keys():
            if not envVars[key]:
                print(key + " -> " + f"{bcolors.FAIL}" +
                      "Not configured" + f"{bcolors.ENDC}" + "\n")
            else:
                print(key + " -> " f"{bcolors.OKGREEN}" +
                      envVars[key] + f"{bcolors.ENDC}" + "\n")
                