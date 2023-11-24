import Data
import random

def percent_delta(is_up):
    if is_up:
        per = round(random.uniform(Data.perc_delta[0], Data.perc_delta[1]) + 1, 4)
    else:
        per = round(random.uniform(-Data.perc_delta[1], Data.perc_delta[0]) + 1, 4)
    return per
def chance_up():
    return Data.chance

def call():
    if random.random() <= chance_up():
        new_p = round(Data.koti[Data.time - 1] * percent_delta(1), 1)
        Data.koti[Data.time] = new_p
        Data.time += 1
    else:
        new_p = round(Data.koti[Data.time - 1] * percent_delta(0), 1)
        Data.koti[Data.time] = new_p
        Data.time += 1

