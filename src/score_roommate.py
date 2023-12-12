import os

import pandas as pd

from src.globals import DATA_DIR_PATH
from src.schema.experiment import SCORERS

df = pd.read_csv(os.path.join(DATA_DIR_PATH, "roommate_benchmark.csv"))

for scorer_name, scorer in SCORERS.items():
    print(f"{scorer_name}: {scorer(y_true=df['true'], y_pred=df['pred'])}")
