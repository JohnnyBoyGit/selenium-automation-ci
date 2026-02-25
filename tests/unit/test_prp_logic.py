# tests/unit/test_prp_logic.py
from src.logic.prp_logic import PrpLogic

def test_prp_constants():
    assert PrpLogic.EXPECTED_TITLE_PART == "PLATELET RICH PLASMA"
    assert "plasma" in PrpLogic.EXPECTED_PATH
