import sys
import platform
import os
import getpass


class OSinteract:
    # Returns true if a environment variable is set inside of a file #
    def variableExists(var, route):
        file = open(route, "r")
        text = file.read()

        return var in text
    
    # Modifies a environment variable that is already written inside of a file #
    def modifyVar(fileRoute, var, content):
        f = open(fileRoute, "r")
        file = f.readlines()

        for line in file:
            if var in line:
                file[file.index(line)] = f"export {var}={content}\n"
                f = open(fileRoute, "w")
                f.writelines(file)
                break
        f.close()

    def cacheFolderExists():
        return os.path.exists(OSinteract.getCurrentDirectory() + "/.cache")

    def pathExists(routeOfFile):
        return os.path.exists(routeOfFile)

    def getAbsolutePath(file):
        return os.path.abspath(file)

    def createFile(routeShell, command):
        os.system(command + " " + routeShell)

    def getUser():
        return getpass.getuser()

    def getCurrentDirectory():
        return os.path.dirname(sys.argv[0])

    def getOS():
        return platform.system()

    def isFile(file):
        return os.path.isfile(file)

    def execute(command):
        return os.system(command)

    def popen(args):
        return os.popen(args)

    def isDir(directory):
        return os.path.isdir(directory)

    def deleteCacheDir(route):
        OSinteract.execute(f"rmdir {route}")

    def createCacheDir(route):
        OSinteract.execute(f"mkdir {route}")

    def exitProgram():
        sys.exit(1) 
