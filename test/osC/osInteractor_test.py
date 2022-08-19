from src.osC.osInteractor import OSinteract
import pathlib

fileConf = ["something very important that DOESN'T have to be deleted",
                "export CYPRESS_RUN_BINARY=route/test", "export CYPRESS_INSTALL_BINARY='0 npm install'", "something important too", 
                "export NODE_EXTRA_CA_CERTS=route/to/cert", "export HTTP_PROXY=https://something.com"]


def test_modify_var(tmp_path: pathlib.PosixPath):
    tmp_path.touch("test.txt")
    file = str(tmp_path.absolute()) + "/test.txt"
    f = open(file, "w")
    for line in fileConf:
        f.write(line + "\n")
    f.close()

    OSinteract.modifyVar(file, "HTTP_PROXY", "test")

    f = open(file, "r")
    fread = f.readlines()
    f.close()

    for line in fileConf:
        if "HTTP_PROXY" in line:
            assert "export HTTP_PROXY=test\n" in fread


def test_check_var(tmp_path: pathlib.PosixPath):
    tmp_path.touch("variableExists.txt")
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    f = open(fileRoute, "w")
    for line in fileConf:
        f.write(line + "\n")
    f.close()

    assert OSinteract.variableExists("CYPRESS_RUN_BINARY", fileRoute)
    assert not OSinteract.variableExists("CYPRESS_CACHE_FOLDER", fileRoute)
