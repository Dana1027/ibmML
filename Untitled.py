#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import os


# In[3]:


os.chdir("C:/Users/hyda1/OneDrive/Winter2021/IBM Machine Learning")


# In[14]:


df = pd.read_csv("FuelConsumptionCo2.csv")

# take a look at the dataset
df.head()


# In[15]:


# summarize the data
df.describe()


# In[16]:


cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(9)


# In[17]:


viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()


# In[18]:


plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()


# In[19]:


plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


# In[20]:


#Plot CYLINDER vs the Emission, to see how linear is their relation:
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Cylinders")
plt.ylabel("Emission")
plt.show()


# In[21]:


msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


# In[23]:


# # Creating train and test dataset
# # Train/Test Split involves splitting the dataset into training and testing sets respectively, 
# which are mutually exclusive. After which, you train with the training set and test with the testing set. 
# This will provide a more accurate evaluation on out-of-sample accuracy because the testing dataset is 
# not part of the dataset that have been used to train the data. It is more realistic for real world problems.

# # This means that we know the outcome of each data point in this dataset, 
# making it great to test with! And since this data has not been used to train the model, 
# the model has no knowledge of the outcome of these data points. So, in essence, it is truly an out-of-sample testing.

# # Lets split our dataset into train and test sets, 80% of the entire data for training, and the 20% for testing. 
# We create a mask to select random rows using np.random.rand() function:

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


# In[24]:


# Simple Regression Model
# Linear Regression fits a linear model with coefficients B = (B1, ..., Bn) to minimize the 'residual sum of squares'
# between the actual value y in the dataset, and the predicted value yhat using linear approximation.

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


# In[26]:


# Modeling
# Using sklearn package to model data.
from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

# As mentioned before, Coefficient and Intercept in the simple linear regression, are the parameters of the fit line. 
# Given that it is a simple linear regression, with only 2 parameters, and knowing that the parameters are the intercept and 
# slope of the line, sklearn can estimate them directly from our data.
# Notice that all of the data must be available to traverse and calculate the parameters.


# In[27]:


# Plot outputs
# We can plot the fit line over the data:

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")


# In[28]:


# Evaluation
# We compare the actual values and predicted values to calculate the accuracy of a regression model. 
# Evaluation metrics provide a key role in the development of a model, 
# as it provides insight to areas that require improvement.

# There are different model evaluation metrics, 
# lets use MSE here to calculate the accuracy of our model based on the test set:

# - Mean absolute error: It is the mean of the absolute value of the errors. 
#     This is the easiest of the metrics to understand since it’s just average error.
# - Mean Squared Error (MSE): Mean Squared Error (MSE) is the mean of the squared error. 
#     It’s more popular than Mean absolute error because the focus is geared more towards large errors. 
#     This is due to the squared term exponentially increasing larger errors in comparison to smaller ones.
# - Root Mean Squared Error (RMSE).
# - R-squared is not error, but is a popular metric for accuracy of your model. 
# It represents how close the data are to the fitted regression line. 
# The higher the R-squared, the better the model fits your data. 
# Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).


# In[29]:


from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )


# In[ ]:




