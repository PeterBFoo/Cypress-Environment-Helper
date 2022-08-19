
class EnvironmentVariables:

    envVars = {"CYPRESS_RUN_BINARY": "",
               "CYPRESS_CACHE_FOLDER": "",
               "HTTP_PROXY": "",
               "CYPRESS_INSTALL_BINARY": "",
               "NODE_EXTRA_CA_CERTS": ""}

    def getEnvironmentVariables():
        return EnvironmentVariables.envVars
