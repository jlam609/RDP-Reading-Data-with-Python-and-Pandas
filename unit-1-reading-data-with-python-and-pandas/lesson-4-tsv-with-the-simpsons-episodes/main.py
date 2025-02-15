import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']
select_cols = ['Title', 'Air date', 'Production code', 'IMDB rating']
simpsons = pd.read_csv(
    "/Users/jasonlam/Desktop/projects/datascience/RDP-Reading-Data-with-Python-and-Pandas/unit-1-reading-data-with-python-and-pandas/lesson-4-tsv-with-the-simpsons-episodes/files/simpsons-episodes.tsv",
    sep='\t', names=col_names, skiprows=4, index_col='Production code', na_values='no_val', parse_dates=['Air date'], usecols=select_cols)
print(simpsons.head())
