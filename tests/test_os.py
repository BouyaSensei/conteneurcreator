
import pytest
import platform

def test_os_detection(mocker):
    # Test pour Windows
    mocker.patch('platform.system', return_value='Windows')
    assert platform.system() == 'Windows'
    
    # Test pour Linux
    mocker.patch('platform.system', return_value='Linux')
    assert platform.system() == 'Linux'
    

