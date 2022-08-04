import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])
model = LinearRegression().fit(x, y)
r_sq = model.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
'''OUTPUT:
coefficient of determination: 
0.715875613747954 
intercept: 5.633333333333333 
slope: [0.54] 
predicted response: 
[ 8.33333333 13.73333333 19.13333333 24.53333333 29.93333333 35.33333333]'''
