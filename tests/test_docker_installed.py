import pytest
import subprocess
import sys
from conteneurcreator import is_docker_installed

def test_is_docker_installed(mocker):
    # Simuler le comportement de subprocess.run
    mock_subprocess = mocker.patch('subprocess.run')
    
    # Tester le cas où Docker est installé
    mock_subprocess.return_value.returncode = 0
    assert is_docker_installed() == True
    
    # Tester le cas où Docker n'est pas installé
    mock_subprocess.side_effect = FileNotFoundError()
    assert is_docker_installed() == False
