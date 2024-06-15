
import pytest
from app.operations import rpn_cal
from app.utils import format_expression

def test_evaluate_expression():
    assert rpn_cal(format_expression("3 50 +")) == 8
    assert rpn_cal(format_expression("2 10 /")) == 5
    assert rpn_cal(format_expression("4 2 *")) == 8

    with pytest.raises(ValueError):
        rpn_cal(format_expression("3 +"))

    with pytest.raises(ValueError):
        rpn_cal(format_expression("3 0 /"))
