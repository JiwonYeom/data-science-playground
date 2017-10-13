import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',60)

df = pd.read_csv('HR_comma_sep.csv')

#initial trial
#print df[:5]

#attempting to sort
df = df.sort_values(['satisfaction_level','time_spend_company'], ascending=[0,1])
#print(dfAcc[['satisfaction_level','time_spend_company','sales']])

#by job field
#total
accTotal = len(df.loc[df["sales"] == 'accounting'].index)
itTotal =len(df.loc[(df["sales"] == 'IT') | (df["sales"] == 'technical')].index)
salesTotal =  len(df.loc[df["sales"] == 'sales'].index)

dfAcc = df.loc[df["sales"] == 'accounting']
dfTech = df.loc[(df["sales"] == 'IT') | (df["sales"] == 'technical')]
accountLong = dfAcc.loc[df["time_spend_company"] > 8]
ITLong = dfTech.loc[df["time_spend_company"] > 8]
salesLong = df.loc[(df["sales"] == 'sales') & (df["time_spend_company"] > 8)]

accLongCnt = len(accountLong.index)
ITLongCnt = len(ITLong.index)
salesLongCnt = len(salesLong.index)

#relative stay rates
print("Account")
print(accLongCnt/accTotal * 100)
print("IT/Tech")
print(ITLongCnt/itTotal * 100)
print("sales")
print(salesLongCnt/salesTotal * 100)