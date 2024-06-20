import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_de_l_inversion_des_variables():
    user_input = ["3", "7"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import Exo1

    output = mock_stdout.getvalue()
    assert "Après inversion :" in output
    assert "v1 vaut : 7" in output
    assert "v2 vaut : 3" in output