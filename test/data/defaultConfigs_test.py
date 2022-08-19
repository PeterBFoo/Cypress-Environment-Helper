from src.data import DefaultConfig
import platform


def test_get_config_param():
    configs = ['CYPRESS_RUN_BINARY_MAC',
               'CYPRESS_RUN_BINARY_WIN', 'CYPRESS_CACHE_FOLDER_MAC', 'CYPRESS_CACHE_FOLDER_WIN', 'HTTP_PROXY']

    for config in configs:
        assert isinstance(DefaultConfig.getVariableValue(config), str)


def test_get_cache_folder_route():
    ### This test depends on which os you are running ###
    opSys = platform.system()

    if opSys.lower() == 'darwin':
        assert DefaultConfig.getCacheFolderRoute(
        ) == DefaultConfig.getVariableValue('CYPRESS_CACHE_FOLDER_MAC')

    elif opSys.lower() == 'windows':
        assert DefaultConfig.getCacheFolderRoute(
        ) == DefaultConfig.getVariableValue('CYPRESS_CACHE_FOLDER_WIN')
