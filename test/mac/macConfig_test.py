from src.mac import Mac
import os
import getpass
import pathlib
import platform
import pytest

envVars = {"CYPRESS_RUN_BINARY": "test1",
               "CYPRESS_CACHE_FOLDER": "test2",
               "HTTP_PROXY": "test3",
               "CYPRESS_INSTALL_BINARY": "test4",
               "NODE_EXTRA_CA_CERTS": "test5"}

@pytest.fixture(scope="module")
def run_before_tests(tmp_path):
    # Creates test.txt inside a tmp file that only stays during the test #
    tmp_path.touch("test.txt")

def test_get_shell_mac():
    shell = Mac.getShellMac()
    assert shell == ".bash_profile" or shell == ".zshrc"

def test_read_shell_mac():
    shellRoute = Mac.getShellPath()
    assert shellRoute == "/Users/" + getpass.getuser() + "/.bash_profile" or "/Users/" + \
        getpass.getuser() + "/.zshrc"

def test_run_binary(tmp_path):
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setRunBinary(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "CYPRESS_RUN_BINARY=" + envVars["CYPRESS_RUN_BINARY"] in fread
        
def test_delete_run_binary_var(tmp_path: pathlib.PosixPath):
    envVars["CYPRESS_RUN_BINARY"] = ""
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setRunBinary(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "CYPRESS_RUN_BINARY=" in fread

def test_install_binary(tmp_path):
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setInstallBinary(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "CYPRESS_INSTALL_BINARY=" + \
        envVars["CYPRESS_INSTALL_BINARY"] in fread
            
def test_delete_install_binary_var(tmp_path: pathlib.PosixPath):
    envVars["CYPRESS_INSTALL_BINARY"] = ""
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setInstallBinary(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "CYPRESS_INSTALL_BINARY=" in fread

def test_http_proxy(tmp_path):
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setHttpProxy(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "HTTP_PROXY=" + envVars["HTTP_PROXY"] in fread
        
def test_delete_http_proxy_var(tmp_path: pathlib.PosixPath):
    envVars["HTTP_PROXY"] = ""
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setHttpProxy(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "HTTP_PROXY=" in fread
    
def test_ca_certs(tmp_path):
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setCaCert(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "NODE_EXTRA_CA_CERTS=" + envVars["NODE_EXTRA_CA_CERTS"] in fread
    
def test_delete_ca_certs_var(tmp_path: pathlib.PosixPath):
    envVars["NODE_EXTRA_CA_CERTS"] = ""
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setCaCert(envVars, fileRoute, f)
    f.close()
    
    fread = pathlib.Path(fileRoute).read_text()
    assert "NODE_EXTRA_CA_CERTS=" in fread

def test_cache_dir(tmp_path: pathlib.PosixPath):
    envVars["CYPRESS_CACHE_FOLDER"] = str(tmp_path.absolute() / ".cache")
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    f = open(fileRoute, "a")
    Mac.setCacheFolder(envVars, fileRoute, f)
    f.close()
    
    # Assert that the CYPRESS_CACHE_FOLDER created inside the tmp dir exists #
    assert os.path.isdir(envVars["CYPRESS_CACHE_FOLDER"])
    
    # Assert that the CYPRESS_CACHE_FOLDER var is set inside the test.txt file #
    fread = pathlib.Path(fileRoute).read_text()
    assert "CYPRESS_CACHE_FOLDER=" + \
        envVars["CYPRESS_CACHE_FOLDER"] in fread

def test_delete_cache_dir_var(tmp_path: pathlib.PosixPath):
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    envVars["CYPRESS_CACHE_FOLDER"] = ""
    
    f = open(fileRoute, "a")
    Mac.setCacheFolder(envVars, fileRoute, f)
    f.close()
    
    # Assert that the CYPRESS_CACHE_FOLDER env is not set inside the test.txt file #
    fread = pathlib.Path(fileRoute).read_text()
    assert "CYPRESS_CACHE_FOLDER=" in fread

def test_env_variables_mac(tmp_path: pathlib.PosixPath):
    envVars["CYPRESS_CACHE_FOLDER"] = str(tmp_path.absolute() / ".cache")
    fileRoute = str(tmp_path.absolute()) + "/test.txt"
    
    Mac.setEnvironmentVariables(fileRoute, envVars)
    fread = pathlib.Path(fileRoute).read_text()
    
    for key in envVars.keys():
        # Assert that test.txt file has the expected writen params in it #
        assert key + "=" + envVars[key] in fread
    
    assert os.path.isdir(envVars["CYPRESS_CACHE_FOLDER"])
