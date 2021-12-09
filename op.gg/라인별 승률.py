import numpy as np
import pandas as pd

match=pd.read_csv('BIPA_data.csv')
cham=pd.read_csv('champ_stats.csv')

md=pd.DataFrame(match,columns=["tierRank","position","championId","result","lane"])
md_lane=md.groupby('result','lane','')