import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',60)

df = pd.read_csv('HR_comma_sep.csv')

#initial trial
#print df[:5]

#attempting to sort
df = df.sort_values(['satisfaction_level','time_spend_company'], ascending=[0,1])
print df[['satisfaction_level','time_spend_company']]

