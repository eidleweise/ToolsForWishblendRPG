import random
import sys


def get_rangeModifier(in_val):
    if in_val in range(0, 10):
        return 0
    if in_val in range(10, 14):
        return 1
    if in_val in range(14, 18):
        return 2
    if in_val in range(18, 21):
        return 3
    if in_val in range(21, 24):
        return 4
    if in_val in range(24, 27):
        return 5
    if in_val in range(27, 30):
        return 6
    if in_val in range(30, 33):
        return 7
    if in_val in range(33, sys.maxsize):
        return 8
    else:
        return -1

def get_discovery_yield(in_val):
    if in_val in range(1, 6):
        return 8000
    if in_val in range(6, 11):
        return 40000
    if in_val in range(11, 16):
        return 180000
    if in_val in range(16, 21):
        return 300000
    if in_val in range(21, 26):
        return 1000000
    if in_val in range(26, sys.maxsize):
        return 3000000

d100 = random.randint(1, 101)

# Basic Discovery Scanner None
# Intermediate Discovery Scanner 2
# Advanced Discovery Scanner 5
# Detailed Planetary Scanner 3
# Planetary Vehicle Hanger with SRV 2
# Fuel Scoop (Any type) 1
# Skill Exploration Val

equip_exploration_bonus = 30 # See Table Above
jump_range = 28
navigation_bonus = 3

jump_range_bonus = get_rangeModifier(jump_range)
calculated_nav_bonus = equip_exploration_bonus + navigation_bonus + jump_range_bonus

exploration_value = get_discovery_yield(calculated_nav_bonus)


# print("I've <{}> years of experience and my salary is <{:,}> USD per annum.".format(10, 75000))

print("Ship Range [{}] credits [{:,}].".format(jump_range, exploration_value))

# print("Ship Range [" + str(jump_range) + "] credits: " + str(exploration_value))
