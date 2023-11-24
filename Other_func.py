import Data


def Text_Balance():
    d = Data.cur_bal - Data.st_bal
    z = '+' if d >= 0 else '-'
    return f"{Data.st_bal}\n{z}{Data.cur_bal - Data.st_bal} / {z}{round(d / Data.st_bal * 100, 2)}%"


def Text_Stock():
    return f"{'Ozon'}\n{Data.koti[Data.time - 1]}, {Data.port['Ozon']} шт."


def Text_cur_price():
    return f"{Data.koti[Data.time - 1]} руб."


def Buy():
    Data.cur_bal -= Data.count_of_deal * Data.koti[Data.time - 1]
    Data.port['Ozon'] += Data.count_of_deal


def Sell():
    Data.cur_bal += Data.count_of_deal * Data.koti[Data.time - 1]
    Data.port['Ozon'] -= Data.count_of_deal


def Plus():
    Data.count_of_deal += 1


def Minus():
    Data.count_of_deal -= 1


def Get_count_of_deal_from_user(c):
    Data.count_of_deal = c
