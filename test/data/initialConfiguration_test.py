from src.data import InitialConfiguration

def test_get_data():
    assert type(InitialConfiguration.getEnvironmentVariables()) is dict


def test_modify_var_conf():
    InitialConfiguration.setVariableConf('HTTP_PROXY', 'TEST-TEST')
    assert InitialConfiguration.getEnvironmentVariables()[
        'HTTP_PROXY'] == 'TEST-TEST'


def test_print_data(capsys):
    InitialConfiguration.printData()
    captured = capsys.readouterr()
    assert 'TEST-TEST' in str(captured)
    
def test_clear_configuration():
    envVars = InitialConfiguration.getEnvironmentVariables()
    for key in envVars.keys():
        envVars[key] = "test"
    
    InitialConfiguration.clearVariablesConf()
    assert len(list(filter(lambda key: envVars[key] == "test", envVars))) == 0
