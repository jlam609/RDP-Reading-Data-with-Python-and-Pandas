import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open('files/van_crime_2003.sql', 'r').read())

late_crimes = pd.read_sql('SELECT * from van_crimes WHERE hour > 18', conn)
dangerous_month_crimes = pd.read_sql('SELECT *, COUNT(*) as TOTAL_PER_MONTH FROM van_crimes GROUP BY month ORDER BY TOTAL_PER_MONTH DESC', conn)
print(dangerous_month_crimes)

# your code goes here
