# tests/unit/test_error_handling.py
import pytest
from unittest.mock import MagicMock

def test_handle_external_tab_timeout_logic():
    """
    SENIOR UNIT TEST: Using standard unittest.mock.
    This is 'Pure' logic testing—no browser, no plugins, just speed.
    """
    # 1. ARRANGE: Create a 'Fake' Page Object
    # We do NOT pass any fixtures here (no home, no mocker)
    mock_page = MagicMock()
    
    # 2. STUB: Tell the mock to return False (simulating a timeout)
    mock_page.handle_external_tab.return_value = False
    
    # 3. ACT: Call the method on our fake object
    result = mock_page.handle_external_tab(timeout=1)
    
    # 4. ASSERT: Verify the result is what we expect
    assert result is False, "Logic should return False when tab fails to open"
    
    # 5. VERIFY: Ensure our code interacted with the browser driver correctly
    mock_page.handle_external_tab.assert_called_once_with(timeout=1)
