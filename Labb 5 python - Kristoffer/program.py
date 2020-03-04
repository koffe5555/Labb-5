import numpy as np
from numpy import percentile
import pandas as pd
import csv, sys
import matplotlib.pyplot as plt
import seaborn as sns

#DF för män
man_df = pd.read_csv('df_table_man.csv', sep=';', names=['år', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
man_df.set_index('år')

#DF för kvinnor
# kvinna_df = pd.read_csv('df_table_kvinna.csv', sep=';', names=['år', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
# kvinna_df.set_index('år')


år_man = man_df
ålder_man = man_df[['år']]

#år_kvinna = kvinna_df[['år', '2000', '2001']]


#Summan av dataframen
totala = man_df[['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']]
p = totala.sum()
print(f'Totala mängden dödsfall för varje år:\n {p}')

#Hsitogram
#plt.figure(figsize=(2, 4))
totala.plot(kind='hist')
#plt.hist(år_man)
plt.xlabel('Dödsfall')
plt.ylabel('ålder')
#plt.tight_layout
plt.show()

#GRAF
# år_man.plot(title='Ålder på dödsfall', kind='line')
# plt.ylabel('Dödsfall')
# plt.xlabel('Ålder')
# plt.show()

#SCATTER 2
# plt.scatter(man_df['år'], man_df['2019'], label="Point", color='r', marker='o', s=10)

# plt.xlabel('Ålder')
# plt.ylabel('Dödsfall')
# plt.title('Dödsfall kopplat till ålder')
# plt.legend()
# plt.show()


#SCATTER
# fig, scat = plt.subplots(figsize=(16, 8))
# scat.scatter(man_df['år'], man_df['2000'], man_df['2009'], man_df['2019'])
# scat.set_xlabel('Ålder')
# scat.set_ylabel('dödsfall')
# plt.show()

#HeatMaps
# correlation_matrix = man_df.corr().round(2)
# sns.heatmap(data=correlation_matrix, annot=True)
# plt.show()

#Ta bort NULL
#df_csv = df_csv.dropna()


#RÄKNA MEDIAN
# median = man_df['2000']
# procent = percentile(median, 25, 50, 75)
# print(f"medianen för åren är : ",(procent))
# low_count = percentile(median, 1)
# high_count = percentile(median, 100)
# print(f"Lägsta dödsantalet", low_count, "st")
# print(f"Högsta dödsantalet", high_count, "st")
