import pytest  # used for our unit tests

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    time_str = ""
    if hours > 0:
        time_str += f"{hours}h"
    if minutes > 0:
        time_str += f"{minutes}min"
    if seconds > 0:
        time_str += f"{seconds}s"
    
    return time_str

#Below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize(
    "seconds, expected",  # the two arguments we are testing for
    [
        (3600, "1h"),  # normal case: 1 hour
        (3661, "1h1min1s"),  # normal case: 1 hour, 1 minute, 1 second
        (7200, "2h"),  # normal case: 2 hours
        (0, ""),  # edge case: 0 seconds
        (-1, ""),  # edge case: -1 seconds
        (-3600, ""),  # edge case: -1 hour
        ("abc", ""),  # special case: a string
        (3.5, ""),  # special case: a float
        (None, ""),  # special case: a NoneType
    ]
)
def test_format_time(seconds, expected):
    assert format_time(seconds) == expected  # assert that the function output matches the expected output

