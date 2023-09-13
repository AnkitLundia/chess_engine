import pandas as pd
import numpy as np
from pgn_parser import pgnParser
from rnn_engine import create_corpus

dataset = pd.read_csv("D:/kaggle comps/chess_engine/GM_games_dataset.csv", nrows=5000)
#all_pgn = dataset['']
c = 0
#print(dataset["pgn"][1])
for i in dataset['pgn']:
    moves = pgnParser(i)
    dataset['pgn'][c] = moves
    c+=1
print(dataset["pgn"][1])
create_corpus(dataset)