from utils.utils import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (3, 3, 1),
                                                   (100, 20, 5),
                                                   (1, 0, "Error.Division by Zero"),
                                                   ("str", 0, "Something wrong"),
                                                   (0, "", "Something wrong"),
                                                   ("str", "0", "Something wrong"),
                                                   (0, 2.0, 0),
                                                   (10, 2.0, 5.0),
                                                   (10, 2.0, 5),
                                                   (1.44, 2.0, 0.72)])
def test_division_v0(a, b, expected_result):
    assert division(a, b) == expected_result



