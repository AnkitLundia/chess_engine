import pandas as pd
import numpy as np
from pgn_parser import pgnParser

dataset = pd.read_csv("D:/kaggle comps/chess_engine/GM_games_dataset.csv", nrows=5000)
#all_pgn = dataset['']
c = 0
for i in dataset['pgn']:
    moves = pgnParser(i)
    print(type(moves))
    break