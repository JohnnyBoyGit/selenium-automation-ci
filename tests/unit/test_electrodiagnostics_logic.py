# tests/unit/test_electrodiagnostics_logic.py
import pytest
from src.logic.electrodiagnostics_logic import ElectroDiagnosticsLogic

def test_electro_title_logic():
    assert "ELECTRODIAGNOSTIC" in ElectroDiagnosticsLogic.EXPECTED_TITLE_PART

@pytest.mark.parametrize("phone_input, expected", [
    ("(818) 555-1234", True),
    ("8185551234", True),
    ("123", False)
])
def test_electro_phone_logic(phone_input, expected):
    assert ElectroDiagnosticsLogic.is_valid_phone_format(phone_input) == expected
