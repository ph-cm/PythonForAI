# Expanding core Python functionality
# for implementation we have a lot of open source libaries for each study area
# Examples:
#     |Dataframes: pandas, polars                     |
#     |Data Visualization: matplotlib, seaborn, plotly|
#     |Machine Learning: sklearn, xgboost             |
#     |Deep Learning: pytorch, tensorflow             |
#     |LLMs, Multi-Modal: transformers, openai        |
#     |Web Stuff: requests, beautifulsoup4            |

# To install the libaries we can use pip that is a Python's package manager

import numpy as np

#create a vector
v = np.array([1, 2, 3])
print(v)

#multiply the vector
print(2*v) #it will multiply each element to 2

#create a matrix
x = np.array([v, 2*v, v/2]) #so it just a vector of vectors
print(x)

v2 = np.array([2, 4, 6, 7]) #if i try to put this vector in a 3x3 matrix, it will occor an error

#matrix multiplication
print(np.matmul(x, v))
