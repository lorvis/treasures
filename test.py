
from hunt_func import hunt_recursive
from hunt_oop import Organization
test_input_correct = [[55, 14, 25, 52, 21],
              [44, 31, 11, 53, 43],
              [24, 13, 45, 12, 34],
              [42, 22, 43, 32, 41],
              [51, 23, 33, 54, 15]]

test_output = [11, 55, 15, 21, 44, 32, 13, 25, 43]

start_pos = "11"


start_hunt_func = hunt_recursive(test_input_correct)


def test_func_correct():
    assert start_hunt_func(start_pos) == test_output


def test_oop_correct():
    org = Organization(test_input_correct, start_pos)
    assert org.hunt() == test_output


