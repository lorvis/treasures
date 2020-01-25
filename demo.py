from hunt_func import hunt_recursive
from hunt_oop import Organization

tres_map = [[31, 21, 32, 41, 25],
              [14, 42, 43, 14, 31],
              [51, 45, 52, 42, 23],
              [33, 15, 51, 31, 35],
              [21, 52, 33, 13, 25]]

start_pos = "11"

hunt = hunt_recursive(tres_map)
print(f"Functional result: {hunt(start_pos)}\n ----------------------------------------------------------")

org = Organization(tres_map, start_pos)
print(f"OOP result: {org.hunt()}")


