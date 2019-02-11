import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cust_df = pd.read_csv("DS_hisshu.csv")

#del(cust_df['Channel'])
#del(cust_df['Region'])
cust_array = np.array([cust_df['N1'].tolist(),
                       cust_df['N2'].tolist(),
                       cust_df['N3'].tolist(),
                       cust_df['N4'].tolist(),
                       cust_df['N5'].tolist(),
                       ], np.int32)
cust_array = cust_array.T
pred = KMeans(n_clusters=5).fit_predict(cust_array)
cust_df['cluster_id']=pred
cust_df['cluster_id'].value_counts()

f = open("cluster.csv", "w")
for i in range(len(pred)):
    f.write(str(pred[i]) + '\n')
f.close()

print(cust_df)
