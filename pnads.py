import numpy as np
from sklearn.preprocessing import StandardScaler
print("blblablablaba")
x = np.array([[1,2,3],
             [4,5,6]])
st = StandardScaler()
st.fit_transform(x)
print(st)
