from src.osC import OSinteract

DEFAULT_CONFIGURATIONS = {"CYPRESS_RUN_BINARY_MAC": "/Applications/Cypress.app/Contents/MacOS/Cypress",
            "CYPRESS_RUN_BINARY_WIN": "C:\\\\Users\\" + OSinteract.getUser() +
            "\\Downloads\\Cypress.exe", "CYPRESS_INSTALL_BINARY": '"0 npm install"',
            "CYPRESS_CACHE_FOLDER_MAC": OSinteract.getCurrentDirectory() + "/.cache",
            "CYPRESS_CACHE_FOLDER_WIN": OSinteract.getCurrentDirectory() + "\\.cache",
            "HTTP_PROXY": "https://nexus.riu.net/repository/",
            "PATH_ENVIRONMENT_FILE_UBUNTU": "/etc/environment"}

VALID_OS_BASH = ["darwin", "ubuntu"]

class DefaultConfig:
    
    def getVariableValue(var):
        return DEFAULT_CONFIGURATIONS[var]

    def getCacheFolderRoute():
        osSys = OSinteract.getOS()

        if osSys.lower() == "windows":
            return DEFAULT_CONFIGURATIONS['CYPRESS_CACHE_FOLDER_WIN']
        else:
            return DEFAULT_CONFIGURATIONS['CYPRESS_CACHE_FOLDER_MAC']

    def getRunBinary():
        osSys = OSinteract.getOS()

        if osSys.lower() == "windows":
            return DEFAULT_CONFIGURATIONS['CYPRESS_RUN_BINARY_WIN']
        else:
            return DEFAULT_CONFIGURATIONS['CYPRESS_RUN_BINARY_MAC']
        
    def getEnvironmentPath():
        return DEFAULT_CONFIGURATIONS["PATH_ENVIRONMENT_FILE_UBUNTU"]

    def getValidOS():
        return VALID_OS_BASH