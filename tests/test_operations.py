
import pytest
from app.operations import rpn_cal
from app.utils import format_expression

def test_evaluate_expression():
    assert rpn_cal("3 5 +") == 8
    assert rpn_cal("10 2 /") == 5
    assert rpn_cal("4 2 *") == 8

    with pytest.raises(ValueError):
        rpn_cal("15 8 * 15 + 3")

    with pytest.raises(ValueError):
        rpn_cal("3 0 /")
