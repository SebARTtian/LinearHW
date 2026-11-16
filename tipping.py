from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

data = np.loadtxt("tips.csv", delimiter=",", dtype = str)
print(data)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

x_units = "bills"
y_units = "tips"
print_equation(slope, intercept, y_units, x_units) #y= 0.18221473222560391 tip/bill + -0.2922674195507699 tip

fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept), label='Linear Fit')
plt.legend(loc='best')
plt.xlabel("bills")
plt.ylabel("tips")
plt.show()
fig.savefig('tippingplot.png')


# 5

x = data[1:, 0].astype(np.float32)
y = data[1:, 6].astype(np.float32)

print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

x_units = "bills"
y_units = "PctTips"
print_equation(slope, intercept, y_units, x_units) #y= 0.04881243455874584 PctTip/bill + 15.509648238069316 PctTips

fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept), label='Linear Fit')
plt.legend(loc='best')
plt.xlabel("bills")
plt.ylabel("PctTips")
plt.show()
fig.savefig('tippingplot.png')
