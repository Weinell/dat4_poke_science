import pandas as pd
from ApiToCsv import read_battles_data
from v2.poke_battle import calc_battles
if __name__ == '__main__':
    calc_battles()
    print('Init')
    print(pd.__version__)
