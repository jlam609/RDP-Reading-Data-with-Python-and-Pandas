import numpy as np
import pandas as pd

colNames = ['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated']
data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'
playstore_df = pd.read_excel(data_url, usecols=colNames, date_parser=['Last_Updated'])
playstore_df = playstore_df.sort_values('Rating', ascending = False).head(25)
print(playstore_df)