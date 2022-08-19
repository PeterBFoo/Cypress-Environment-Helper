from src.app.app import *
from src.app.configureVariables import *
from src.data.initialVarsConfiguration import InitialConfiguration
from src.osC.osInteractor import OSinteract
import inquirer

OP_SYS = OSinteract.getOS().lower()


def initEnvConfiguration():

    if OP_SYS in DefaultConfig.getValidOS():

        questions = [
            inquirer.Checkbox('envVars',
                              message="Which environment variables do you wish to set? (use the -> key on your keyboard to select)",
                              choices=["CYPRESS_CACHE_FOLDER", "CYPRESS_RUN_BINARY", "CYPRESS_INSTALL_BINARY", "HTTP_PROXY", "NODE_EXTRA_CA_CERTS"])
        ]
        answer = inquirer.prompt(questions)

        configurationOptions(answer)

    else:
        configureAll()


def configurationOptions(options):
    for option in options["envVars"]:
        if option == "CYPRESS_CACHE_FOLDER":
            ConfigureEnvVariables.configureCache(OP_SYS)
        elif option == "CYPRESS_RUN_BINARY":
            ConfigureEnvVariables.configureRunBinary(OP_SYS)
        elif option == "HTTP_PROXY":
            ConfigureEnvVariables.configureProxy()
        elif option == "CYPRESS_INSTALL_BINARY":
            ConfigureEnvVariables.configureInstallBinary()
        elif option == "NODE_EXTRA_CA_CERTS":
            ConfigureEnvVariables.configureCert()
    InitialConfiguration.printData()
    checkCorrect()


def configureAll():
    ConfigureEnvVariables.configureCache(OP_SYS)
    ConfigureEnvVariables.configureRunBinary(OP_SYS)
    ConfigureEnvVariables.configureProxy()
    ConfigureEnvVariables.configureCert()
    ConfigureEnvVariables.configureInstallBinary()
    InitialConfiguration.printData()
    checkCorrect()


def checkCorrect():
    changeConfig = input(
        "\nIs everything correct? y/n (enter 'q' to exit): ")

    if changeConfig == "y":
        App.initApp(InitialConfiguration.getEnvironmentVariables())
    elif changeConfig == "n":
        InitialConfiguration.clearVariablesConf()
        initEnvConfiguration()
    elif changeConfig == "q":
        OSinteract.exitProgram()
    else:
        WarningCy.warning("checkCorrect")
        checkCorrect()


if __name__ == "__main__":
    initEnvConfiguration()
