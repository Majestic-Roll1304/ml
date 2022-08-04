import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/KMITDS/CS601PC/main/individual.csv")
#print(df.head(10))
# we need to find P(recreation=golf) and P(status=single/credit-worthiness=medRisk)
# Pr(status='single'| credit-worthiness='medRisk') = Pr(status='single' & creditworthiness='medRisk') / Pr(credit-worthiness='medRisk')
df[(df.status=='single') & (df.cw=='medRisk')]
df.columns
df[(df.cw=='medRisk')]
print("P(recreation=golf)")
print(df[(df.recreation=='golf')].shape[0]/df.shape[0])
print(" P(status=single/credit-worthiness=medRisk)")
print(df[(df.status=='single') & (df.cw=='medRisk')].shape[0]/df[(df.cw=='medRisk')].shape[0])

'''
OUTPUT:
P(recreation=golf) 
0.4 
P(status=single/credit-
worthiness=medRisk) 
0.6666666666666666'''
