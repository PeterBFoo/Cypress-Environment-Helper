from src.mac.macConfig import Mac
from src.data import FinalConfiguration


class MacInterface:

    def initiateConfiguration(varConfig):
        Mac.mac(varConfig)

    def printEnvsConfigMac():
        FinalConfiguration.printEnvConfig()
