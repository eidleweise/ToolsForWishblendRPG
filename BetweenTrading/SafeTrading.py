import random


def get_value(in_val):
    if in_val in range(1, 6):
        return 500
    if in_val in range(5, 16):
        return 600
    if in_val in range(15, 26):
        return 700
    if in_val in range(25, 36):
        return 800
    if in_val in range(36, 46):
        return 900
    if in_val in range(46, 76):
        return 1000
    if in_val in range(76, 81):
        return 1100
    if in_val in range(81, 86):
        return 1200
    if in_val in range(86, 91):
        return 1300
    if in_val in range(91, 96):
        return 1400
    if in_val in range(96, 101):
        return 1500
    else:
        return -1


d100 = random.randint(1, 101)
asp_cargo = 80
type6_cargo = 104
conda_cargo = 432
trade_bonus = 3
profit_per_ton = get_value(d100)

cargo = conda_cargo


trade_credits = profit_per_ton * trade_bonus * cargo
print("D100 [{}] profit_per_ton [{:,}] credits [{:,}].".format(d100, profit_per_ton, trade_credits))
