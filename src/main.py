import pandas as pd
from src.api_file_handler import read_battles_data
from v1.poke_battle import calc_battles
if __name__ == '__main__':

    calc_battles()
    print('Init')
    print(pd.__version__)
