from src.osC import OSinteract
from src.errors import WarningCy
from src.data import DefaultConfig, InitialConfiguration


class ConfigureEnvVariables:
    def configureCache(opSys):
        cacheBool = input("\nCypress may need a cache folder other that the one used by your OS due to permissions problems.\n Normally, you will not need to set this to true, by default. ¿Do you want to create one? y/n: ")

        if cacheBool == "y":
            InitialConfiguration.setVariableConf(
                'CYPRESS_CACHE_FOLDER', DefaultConfig.getCacheFolderRoute())
        elif cacheBool == "n":
            InitialConfiguration.setVariableConf('CYPRESS_CACHE_FOLDER', "")

        else:
            ConfigureEnvVariables.configureCache(opSys)

    def configureProxy():
        needProxyConf = input(
            "\nIf you are behind a proxy, indicate the URL of your proxy (press enter to skip). \n-> ")

        if needProxyConf:
            InitialConfiguration.setVariableConf("HTTP_PROXY", needProxyConf)

    def configureCert():
        ca_cert = input(
            '\nIf you are behind a proxy, you may need a certificate. \nIndicate the absolute route where you have it. If you don\'t need one, you can just press enter. \n-> ')

        if not ca_cert:
            InitialConfiguration.setVariableConf(
                'NODE_EXTRA_CA_CERTS', ca_cert)

        elif OSinteract.isFile(ca_cert):
            InitialConfiguration.setVariableConf(
                'NODE_EXTRA_CA_CERTS', OSinteract.getAbsolutePath(ca_cert))
        else:
            WarningCy.warning('RouteDoesntExist', ca_cert)
            ConfigureEnvVariables.configureCert()

    def configureRunBinary(opSys):
        CYPRESS_RUN_BINARY = input(
            "\nIntroduce the route where you have Cypress installed.\nRoute by default, is: \n macOS -> " + DefaultConfig.getVariableValue("CYPRESS_RUN_BINARY_MAC") + "\n Windows -> " + DefaultConfig.getVariableValue("CYPRESS_RUN_BINARY_WIN") + "\n-> ")

        if not CYPRESS_RUN_BINARY:
            if not OSinteract.isFile(DefaultConfig.getRunBinary()):
                WarningCy.warning("RouteDoesntExist",
                                  DefaultConfig.getRunBinary())
                ConfigureEnvVariables.configureRunBinary(opSys)
            else:
                InitialConfiguration.setVariableConf(
                    'CYPRESS_RUN_BINARY', DefaultConfig.getRunBinary())
        else:
            if not OSinteract.isFile(CYPRESS_RUN_BINARY):
                WarningCy.warning("RouteDoesntExist", CYPRESS_RUN_BINARY)
                ConfigureEnvVariables.configureRunBinary(opSys)
            else:
                InitialConfiguration.setVariableConf(
                    'CYPRESS_RUN_BINARY', CYPRESS_RUN_BINARY)

    def configureInstallBinary():
        CYPRESS_INSTALL_BINARY = input(
            "\nIf you want to set a diferent value for CYPRESS_INSTALL_BINARY, type it.\n By default the value is " + DefaultConfig.getVariableValue("CYPRESS_INSTALL_BINARY") + ", that parameter tells Cypress that you don't want to install any version of Cypress,\n just for the one you have already downloaded (press enter if you just want he one by default)\n -> ")

        if CYPRESS_INSTALL_BINARY != "":
            InitialConfiguration.setVariableConf(
                'CYPRESS_INSTALL_BINARY', CYPRESS_INSTALL_BINARY)
        else:
            InitialConfiguration.setVariableConf(
                'CYPRESS_INSTALL_BINARY', DefaultConfig.getVariableValue('CYPRESS_INSTALL_BINARY'))
