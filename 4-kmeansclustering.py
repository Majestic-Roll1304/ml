import numpy as np
from sklearn.cluster import KMeans
X2=np.array([[1.713,1.586],[0.18,1.786],[0.353,1.24],[0.94,1.566],[1.486,0.759],[1.266,1.106],[1.54,0.419],[0.459,1.799],[0.773,0.186],[0.906,0.606]])
#print(X2)
kmeans = KMeans(n_clusters=3,random_state=13)
kmeans.fit(X2)
centroid = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroid)
print(labels)
for i in range(len(X2)):
    print ("coordinate:" , X2[i], "label:", labels[i])
'''OUTPUT:
[[1.30633333 1.41933333] 
[1.17625 0.4925 ] 
[0.33066667 1.60833333]] [0 
2 2 0 1 0 1 2 1 1] 
coordinate: [1.713 1.586] label: 0 
coordinate: [0.18 1.786] label: 2 
coordinate: [0.353 1.24 ] label: 2 
coordinate: [0.94 1.566] label: 0 
coordinate: [1.486 0.759] label: 1 
coordinate: [1.266 1.106] label: 0 
coordinate: [1.54 0.419] label: 1 
coordinate: [0.459 1.799] label: 2 
coordinate: [0.773 0.186] label: 1 
coordinate: [0.906 0.606] label: 1'''
