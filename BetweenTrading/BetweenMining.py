import random


def get_value(in_val):
    if in_val in range(1, 6):
        return 200
    if in_val in range(5, 16):
        return 400
    if in_val in range(15, 26):
        return 600
    if in_val in range(25, 36):
        return 800
    if in_val in range(36, 46):
        return 900
    if in_val in range(46, 76):
        return 1000
    if in_val in range(76, 81):
        return 1200
    if in_val in range(81, 86):
        return 1400
    if in_val in range(86, 91):
        return 1600
    if in_val in range(91, 96):
        return 1800
    if in_val in range(96, 101):
        return 2000
    else:
        return -1


d100 = random.randint(1, 101)
cobra_mining_bonus = 40 + 7 + 7 + 2
cobra_cargo = 16
type6_mining_bonus = 45 + 14 + 7 + 2
type6_cargo = 64
planetary_knowledge = 3
mining_yield = get_value(d100)


mining_bonus = type6_mining_bonus
cargo = type6_cargo


mining_credits = ((mining_bonus + cargo) * planetary_knowledge) * mining_yield
print("D100 [{}] credits [{:,}].".format(d100, mining_credits))