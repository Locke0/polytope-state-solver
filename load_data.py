import numpy as np
import pandas as pd
from ast import literal_eval
from pathlib import Path
from pprint import pprint
from sympy.combinatorics import Permutation

data_dir = Path("../data")

puzzle_info = pd.read_csv(data_dir / 'puzzle_info.csv', index_col='puzzle_type')
# Parse allowed_moves
puzzle_info['allowed_moves'] = puzzle_info['allowed_moves'].apply(literal_eval)

puzzles = pd.read_csv(data_dir / 'puzzles.csv', index_col='id')
# Parse color states
puzzles = puzzles.assign(
    initial_state=lambda df: df['initial_state'].str.split(';'),
    solution_state=lambda df: df['solution_state'].str.split(';')
)

sample_submission = pd.read_csv(data_dir / 'sample_submission.csv', index_col='id')