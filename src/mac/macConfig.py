from src.osC import OSinteract
from src.data import DefaultConfig


class Mac:

    def __getShell():
        shell = OSinteract.popen('echo ${SHELL}')
        shellRead = shell.read()
        return shellRead

    # Returns the shell that the macOS uses
    def getShellMac():
        shellRead = Mac.__getShell()

        if 'bash' in shellRead:
            return '.bash_profile'
        elif 'zsh' in shellRead:
            return '.zshrc'

    # Returns the route of the bash_profile or zshrc
    def getShellPath():
        shellRead = Mac.getShellMac()
        shellRoute = '/Users/' + OSinteract.getUser() + '/' + shellRead
        return shellRoute

    def setRunBinary(varConfig, fileRoute, f):
        CYPRESS_RUN_BINARY = varConfig['CYPRESS_RUN_BINARY']

        if not OSinteract.variableExists('CYPRESS_RUN_BINARY', fileRoute):
            f.write(f'export CYPRESS_RUN_BINARY={CYPRESS_RUN_BINARY}\n')
        else:
            OSinteract.modifyVar(
                fileRoute, 'CYPRESS_RUN_BINARY', CYPRESS_RUN_BINARY)

    def setCacheFolder(varConfig, fileRoute, f):
        CYPRESS_CACHE_FOLDER = varConfig['CYPRESS_CACHE_FOLDER']

        # Checks if the variable exists inside of the file, even if that var is 'not configured',
        # writes the var inside the bash_profile or zshrc as: export CYPRESS_CACHE_FOLDER=
        if not OSinteract.variableExists('CYPRESS_CACHE_FOLDER', fileRoute):
            f.write(
                f'export CYPRESS_CACHE_FOLDER={CYPRESS_CACHE_FOLDER}\n')

        if (not CYPRESS_CACHE_FOLDER) and OSinteract.isDir(DefaultConfig.getCacheFolderRoute()):
            OSinteract.deleteCacheDir(DefaultConfig.getCacheFolderRoute())

        elif not OSinteract.isDir(CYPRESS_CACHE_FOLDER):
            OSinteract.createCacheDir(CYPRESS_CACHE_FOLDER)

        # Changes the current value for the new one, it can be "" or a route
        OSinteract.modifyVar(
            fileRoute, 'CYPRESS_CACHE_FOLDER', CYPRESS_CACHE_FOLDER)

    def setInstallBinary(varConfig, fileRoute, f):
        CYPRESS_INSTALL_BINARY = varConfig['CYPRESS_INSTALL_BINARY']

        if not OSinteract.variableExists('CYPRESS_INSTALL_BINARY', fileRoute):
            f.write(
                f'export CYPRESS_INSTALL_BINARY={CYPRESS_INSTALL_BINARY}\n')
        else:
            OSinteract.modifyVar(
                fileRoute, 'CYPRESS_INSTALL_BINARY', CYPRESS_INSTALL_BINARY)

    def setHttpProxy(varConfig, fileRoute, f):
        HTTP_PROXY = varConfig['HTTP_PROXY']

        if not OSinteract.variableExists('HTTP_PROXY', fileRoute):
            f.write(f'export HTTP_PROXY={HTTP_PROXY}\n')
        else:
            OSinteract.modifyVar(
                fileRoute, 'HTTP_PROXY', HTTP_PROXY)

    def setCaCert(varConfig, fileRoute, f):
        NODE_EXTRA_CA_CERTS = varConfig['NODE_EXTRA_CA_CERTS']
        if not OSinteract.variableExists('NODE_EXTRA_CA_CERTS', fileRoute):
            f.write(f'export NODE_EXTRA_CA_CERTS={NODE_EXTRA_CA_CERTS}\n')
        else:
            OSinteract.modifyVar(
                fileRoute, 'NODE_EXTRA_CA_CERTS', NODE_EXTRA_CA_CERTS)

    def setEnvironmentVariables(shellRoute, varConfig):
        file = open(shellRoute, 'a')

        Mac.setRunBinary(varConfig, shellRoute, file)
        Mac.setInstallBinary(varConfig, shellRoute, file)
        Mac.setCacheFolder(varConfig, shellRoute, file)
        Mac.setHttpProxy(varConfig, shellRoute, file)
        Mac.setCaCert(varConfig, shellRoute, file)

        file.close()

    def mac(varConfig):
        # Read which shell OS uses #
        shellRoute = Mac.getShellPath()

        # Creates .bash_profile or .zshrc if it doesn't exist #
        if not OSinteract.pathExists(shellRoute):
            OSinteract.createFile(shellRoute, 'touch')

        Mac.setEnvironmentVariables(shellRoute, varConfig)
