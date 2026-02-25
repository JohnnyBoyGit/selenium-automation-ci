# tests/unit/test_common_logic.py
from src.logic.common_logic import CommonLogic

def test_common_phone_logic():
    assert CommonLogic.is_valid_phone_format("(818) 555-1212") is True
    assert CommonLogic.is_valid_phone_format("123") is False
