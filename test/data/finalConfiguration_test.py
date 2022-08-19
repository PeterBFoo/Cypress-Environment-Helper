from src.data import FinalConfiguration


def test_get_data():
    assert type(FinalConfiguration.getEnvironmentVariables()) is dict


def test_print_data(capsys):
    FinalConfiguration.getEnvironmentVariables()['HTTP_PROXY'] = 'TEST-TEST'
    FinalConfiguration.printData()
    capturedOutput = capsys.readouterr()
    assert 'TEST-TEST' in str(capturedOutput)
