from numpy import random
import pandas as pd

n = 1000
random.seed(42)

df = pd.DataFrame({"x": random.normal(size = n)})

df['y'] = 1 + 1.5 * df['x'] + random.normal(size = n)

print(df.head())

import matplotlib.pyplot as plt

plt.scatter(df['x'], df['y'], color = "#154957", alpha = 0.2)
plt.show()

import statsmodels.api as sm

modelo = sm.OLS(df.y, df.x).fit()

print(modelo.summary())
